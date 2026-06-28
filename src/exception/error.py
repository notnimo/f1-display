from abc import ABC, abstractmethod

from src.exception.logger import ErrorLevel, LogLevel


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
  def level():
    return ErrorLevel.ERROR

  @abstractmethod
  def getLogLevel(self) -> LogLevel:
    pass

class Warning(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.WARNING

  @abstractmethod
  def getLogLevel(self) -> LogLevel:
    pass


class Debug(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.DEBUG

  @abstractmethod
  def getLogLevel(self) -> LogLevel:
    pass
