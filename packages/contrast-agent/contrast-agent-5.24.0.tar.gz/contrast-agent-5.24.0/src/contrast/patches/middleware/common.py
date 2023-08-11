# -*- coding: utf-8 -*-
# Copyright © 2023 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
import inspect
from typing import Optional
from enum import Enum, auto

from contrast.agent.policy import patch_manager
from contrast.utils.patch_utils import build_and_apply_patch
from contrast_vendor import structlog as logging
from contrast_vendor.wrapt import register_post_import_hook

logger = logging.getLogger("contrast")


class AppInterfaceType(Enum):
    WSGI = auto()
    ASGI = auto()
    AUTO_DETECT = auto()


def _set_detected_framework(framework_name: str):
    logger.info("Automatically applying %s instrumentation", framework_name)
    from contrast.agent.agent_state import set_detected_framework

    set_detected_framework(framework_name)


def _get_proxy(new_instance, interface: AppInterfaceType):
    from contrast.agent.asgi_proxy import ASGIApplicationProxy
    from contrast.agent.wsgi import WSGIApplicationProxy

    if interface == AppInterfaceType.ASGI:
        proxy = ASGIApplicationProxy
    elif interface == AppInterfaceType.WSGI:
        proxy = WSGIApplicationProxy
    else:
        proxy = (
            ASGIApplicationProxy
            if inspect.iscoroutinefunction(new_instance.__call__)
            else WSGIApplicationProxy
        )

    logger.info(
        f"Application interface: {'ASGI' if proxy == ASGIApplicationProxy else 'WSGI'}"
    )
    return proxy


def build__new__patch(
    orig_func, patch_policy, framework_name: str, interface: AppInterfaceType
):
    """
    Generic patch for __new__ method of various application classes

    This performs automatic middleware installation.
    """
    del patch_policy

    def __new__patch(cls, *args, **kwargs):
        """
        This is a very strange-looking patch. All of the confusing bits are the result
        of the automagic sequence of events that Python performs (in C) when a new
        object is constructed. For some details, see the documentation:

        https://docs.python.org/3/reference/datamodel.html#object.__new__

        For _all_ the details, try to decipher the source code:

        cpython/Objects/typeobject.c

        Q: "Why do we call orig_func without args/kwargs?"
        A: In this case, orig_func is object.__new__. This function accepts exactly one
            argument - the type about to be instantiated. The constructor only accepts
            args and kwargs so it can pass these to __init__.

        Q: "Why do we have to call __init__ in this patch?"
        A: Usually, __init__ is called after __new__ returns the new instance. However,
            there is a condition (in the docs):
            > If __new__() does not return an instance of cls, then the new instance's
            > __init__() method will not be invoked.
            In this patch, we're returning a proxy, not the original object. Apparently,
            the internal python machinery responsible for deciding if __init__ needs to
            be called or not is -not- fooled by the proxy. This means that if we don't
            call __init__ in this patch, it'll never be called at all, and the application
            instance will be hopelessly broken.

        Q: "Can we use @wrapt.function_wrapper?"
        A: Apparently not. Because object.__new__ is a builtin, something internal to
            wrapt fails when we try this. It's totally possible that I've missed some
            detail, but I wasn't able to get it to work after playing around with it.
        """
        from contrast.agent.agent_state import automatic_middleware

        new_instance = orig_func(cls)
        new_instance.__init__(*args, **kwargs)

        # NOTE: if additional functionality is eventually required here, we can
        # pass it as an additional callback to build__new__patch.
        _set_detected_framework(framework_name)
        proxy = _get_proxy(new_instance, interface)

        with automatic_middleware():
            return proxy(new_instance)

    return __new__patch


class CommonMiddlewarePatch:
    """
    Class that implements generic application patches for a variety of frameworks

    We expect that this class can potentially be used in any framework where
    the __new__ method of the framework's application class will be used for
    automatic instrumentation.

    :param module_name: Name of the module that owns the application class
    :param framework_name: Name of the framework (defaults to `module_name`)
    :param application_class_name: Name of the application class to be hooked (defaults to capitalized `framework_name`)
    """

    def __init__(
        self,
        module_name: str,
        *,
        application_class_name: Optional[str] = None,
        framework_name: Optional[str] = None,
        interface: AppInterfaceType = AppInterfaceType.WSGI,
    ):
        self.module_name = module_name
        self.framework_name = framework_name or module_name
        self.application_class_name = (
            application_class_name or self.framework_name.capitalize()
        )
        self.interface = interface

    @property
    def __name__(self):
        return f"{__name__.rpartition('.')[0]}.{self.module_name}"

    def register_patches(self):
        """
        Registers post-import hook for the __new__ method of the application class
        """

        def patch_application(module):
            build_and_apply_patch(
                getattr(module, self.application_class_name),
                "__new__",
                build__new__patch,
                builder_args=(
                    self.framework_name,
                    self.interface,
                ),
            )

        register_post_import_hook(patch_application, self.module_name)

    def reverse_patches(self):
        """
        Reverses patches for the __new__ method of the application class
        """
        patch_manager.reverse_class_patches_by_name(
            self.module_name,
            self.application_class_name,
        )
