from functools import wraps

from flask import Response, request

from Bdays.exceptions.message_not_send import MessageNotSendError


def convert_input_to(class_):
    def wrap(f):
        def decorator(*args):
            obj = class_(**request.get_json())
            return f(obj)
        return decorator
    return wrap


def exception_handler(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            return Response('text', status=500)
    return wrapped
