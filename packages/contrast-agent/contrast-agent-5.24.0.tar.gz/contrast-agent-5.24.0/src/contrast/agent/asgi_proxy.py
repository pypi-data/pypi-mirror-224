# -*- coding: utf-8 -*-
# Copyright © 2023 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
from typing import Callable, Awaitable

from contrast.asgi.middleware import ASGIMiddleware
from contrast.utils.object_utils import BindingObjectProxy


class ASGIApplicationProxy(BindingObjectProxy):
    """
    Wraps an ASGI application callable to apply our middleware. Anything defined as an
    ASGI 3.0 application object (https://asgi.readthedocs.io/en/latest) can be proxied
    by this object.

    This is implemented as a wrapt object proxy. A proxied ASGI application can safely
    replace the original ASGI application even if more framework-level operations still
    need to be performed with the application object (such as route registration,
    configuration, etc).

    This is for internal auto-instrumentation use only. Customers should use the
    ASGIMiddleware directly.
    """

    cs__middleware = None

    def __init__(self, wrapped: Callable[..., Awaitable[None]]) -> None:
        super().__init__(wrapped)
        self.cs__middleware = getattr(
            wrapped, "cs__middleware", ASGIMiddleware(wrapped)
        )

    async def __call__(self, scope, receive, send) -> None:
        assert self.cs__middleware is not None
        await self.cs__middleware(scope, receive, send)

    def run_task(self, *args, **kwargs):
        """
        This method is necessary for instrumenting quart applications that are served with hypercorn.

        It serves the same purpose as `BindingObjectProxy.run` but since it is specific to Quart (ASGI)
        applications it is implemented here.
        """
        if type(self) is type(self.__wrapped__):
            return self.__wrapped__.run_task(*args, **kwargs)
        return self.__wrapped__.run_task.__func__(self, *args, **kwargs)
