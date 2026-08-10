from enum import Enum

class ExceptionLevel(Enum):
    """Enum class for exception levels"""
    INFO = 1
    WARNING = 2
    ERROR = 3
    TERMINATE = 4

class Exception():
    """base exception class for all exceptions in the project"""

    def __init__(self, message: str, level: ExceptionLevel):
        self.message = message
        self.level = level

    def __str__(self):
        return f"{self.level.name}: {self.message}"