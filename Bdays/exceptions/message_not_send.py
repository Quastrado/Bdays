from Bdays.exceptions.server_exception import ServerException


class MessageNotSendError(ServerException):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'MessageNotSendError has been raised'