# -*- coding: utf-8 -*-
# Copyright © 2023 Contrast Security, Inc.
# See https://www.contrastsecurity.com/enduser-terms-0317a for more details.
from typing import Callable

from contrast.utils.object_utils import BindingObjectProxy
from contrast.wsgi.middleware import WSGIMiddleware


class WSGIApplicationProxy(BindingObjectProxy):
    """
    Wraps a WSGI application callable to apply our middleware. Anything defined as a
    PEP-333(3) WSGI application object can be proxied by this object. It doesn't matter
    if the object is a function, class instance with `__call__`, or something else, as
    long as it's a valid callable WSGI application.

    This is implemented as a wrapt object proxy. A proxied WSGI application can safely
    replace the original WSGI application even if more framework-level operations still
    need to be performed with the application object (such as route registration,
    configuration, etc).

    This is for internal auto-instrumentation use only. Customers should use the
    WSGIMiddleware directly.
    """

    cs__middleware = None

    def __init__(self, wrapped: Callable) -> None:
        super().__init__(wrapped)
        self.cs__middleware = getattr(
            wrapped, "cs__middleware", WSGIMiddleware(wrapped)
        )

    def __call__(self, environ, start_response):
        assert self.cs__middleware is not None
        return self.cs__middleware(environ, start_response)
