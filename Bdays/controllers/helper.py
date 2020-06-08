from functools import wraps

from flask import Response, request

from Bdays.exceptions.client_exception import ClientException
from Bdays.exceptions.message_not_send import MessageNotSendError
from Bdays.exceptions.server_exception import ServerException


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
        except ServerException as e:
            return Response('Server', status=500)
        except ClientException as e:
            return Response('Client', status=400)
        except Exception as e:
            return Response('Error', status=500)
    return wrapped
