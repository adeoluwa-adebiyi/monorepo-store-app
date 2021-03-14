from modules.exceptions.app_exception import AppException


class InsufficientProductQuantityError(AppException):

    def __init__(self, message:str):
        super()
        self.message = message

    def __str__(self):
        return self.message


class DuplicateTransactionPaymentException(AppException):

    def __init__(self, message:str):
        super()
        self.message = message

    def __str__(self):
        return self.message

