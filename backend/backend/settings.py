from .base_settings import *
DEBUG = True

if DEBUG:
    MIDDLEWARE.append('backend.middleware.DevProxyMiddleware')
    UPSTREAM = "http://127.0.0.1:8080"