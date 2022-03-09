"""
User Defined Exception will always be a class
It should inherit any of built-in exceptions provide by python
Generally you will be using the base class as
RuntimeError or Exception
"""
class NetworkError(RuntimeError):
    def __init__(self, message):
        self.message = message

raise NetworkError("There was a network error")