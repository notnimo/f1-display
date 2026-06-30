from abc import ABC, abstractmethod

from src.exception.logger import ErrorLevel, LogLevel


class GenericError(ABC):
  @abstractmethod
  def msg(self) -> str:
    pass

  def what(self) -> str:
    return self.msg()


class BaseError(GenericError):
  pass
  

class Error(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.ERROR


class Warning(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.WARNING


class Debug(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.DEBUG
