# -*- coding: utf-8 -*-
# Copyright © 2023 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
from contrast_vendor import wrapt

import copy
import inspect

NOTIMPLEMENTED_MSG = "This method should be implemented by concrete subclass subclass"


def safe_copy(value):
    """
    Return a safe copy of a value

    :param value: to be copied
    :return: copied value if no exception
    """
    try:
        return copy.copy(value)
    except Exception:
        return value


def get_name(obj):
    return f"{obj.__module__}.{obj.__name__}" if inspect.isclass(obj) else obj.__name__


class BindingObjectProxy(wrapt.ObjectProxy):
    """
    This class changes the default behavior of wrapt's ObjectProxy when accessing
    certain bound methods of the proxied object.

    Normally, if we access a bound method of a proxied object, the `self` passed to that
    method will be the wrapped object, not the proxy itself. This means that inside of
    bound methods, we lose the proxy, and the function is allowed to use the un-proxied
    version of the object. This is usually not desirable.

    This class provides a workaround for this behavior, but only for functions that we
    explicitly override here. We haven't come up with a general safe solution to this
    problem for all functions (yet).

    We've tried overriding __getattr__ to try to rebind bound methods on-the-fly as
    they're accessed. This had a bad interaction with BoundFunctionWrapper, which
    returns the original (unwrapped) function when accessing `__func__`.

    With each of the methods defined here, we're making the following assumptions:
    - the underlying object does not have an attribute of the same name OR
    - if the underlying object has an attribute of the same name, that attribute is an
      instance method
    If this doesn't hold, it could lead to very strange / incorrect behavior.
    """

    def run(self, *args, **kwargs):
        if type(self) is type(self.__wrapped__):
            return self.__wrapped__.run(*args, **kwargs)
        return self.__wrapped__.run.__func__(self, *args, **kwargs)
