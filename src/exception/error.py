from abc import ABC, abstractmethod

from src.exception.logger import ErrorLevel


class GenericError(ABC):
    @abstractmethod
    def msg(self) -> str:
        pass

    def what(self) -> str:
        return self.msg()


class BaseError(GenericError):
    def __init__(self, msg: str):
        self._msg = msg

    def msg(self) -> str:
        return self._msg


class Error(BaseError):
    @staticmethod
    def level() -> str:
        return ErrorLevel.ERROR


class Warning(BaseError):
    @staticmethod
    def level() -> str:
        return ErrorLevel.WARNING
