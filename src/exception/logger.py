from enum import Enum


class LogLevel(Enum):
    FULL = 0
    SHORT = 1
    SILENT = 2


class SuppressionLevel(Enum):
    ACTIVE = 0
    SUPPRESSED = 1


class ErrorLevel(Enum):
    WARNING = 0
    ERROR = 1
    DEBUG = 2


class DebugLogger:
    def __init__(self, strbuf: str):
        self._strbuf = strbuf
        print(f"DebugLogger initialized with strbuf: {strbuf}")

    def log(self, message: str):
        print(f"{self._strbuf} {message}")

    def __del__(self):
        print(f"DebugLogger destroyed: {self._strbuf}")


debug: DebugLogger = DebugLogger("F1 display debug > ")
