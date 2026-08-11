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

class Logger:
    def __init__(self, name: str):
        self.name = name
        print(f"--------------------------\nLogger initialized for {self.name}\n--------------------------")

    def log(self, error: Exception):
        match(error.level):
            case ExceptionLevel.INFO:
                print(f"[{self.name}]: INFO: {error.message}")
            case ExceptionLevel.WARNING:
                print(f"[{self.name}]: WARNING: {error.message}")
            case ExceptionLevel.ERROR:
                print(f"[{self.name}]: ERROR: {error.message}")
            case ExceptionLevel.TERMINATE:
                print(f"[{self.name}]: TERMINATE: {error.message}")
#                exit(1)

debug: Logger = Logger("F1-disp-logger")