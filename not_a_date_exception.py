class NotADateException(Exception):
    def __init__(self, msg='Value is not of type DateTime'):
        self.msg = msg

    def __str__(self):
        return self.msg