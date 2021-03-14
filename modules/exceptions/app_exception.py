class AppException(Exception):

    def __init__(self, message:str):
        super(message)
        self.message = message

    def get_message(self):
        return self.message
