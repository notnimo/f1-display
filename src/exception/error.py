from abc import ABC, abstractmethod

from src.exception.logger import ErrorLevel, LogLevel


class GenericError(ABC):
  @abstractmethod
  def msg(self) -> str:
    pass

  def what(self) -> str:
    return self.msg()


class BaseError(GenericError):
  @abstractmethod
  def getS() -> str:
    pass

  @abstractmethod
  def compose(self) -> str:
    pass

  def msg(self) -> str:
    return self.compose()
  
  @abstractmethod
  def level() -> ErrorLevel:
    pass

  @abstractmethod
  def getLogLevel(self) -> LogLevel:
    pass
  

class Error(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.ERROR

  def getLogLevel(self) -> LogLevel:
    pass

class Warning(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.WARNING

  def getLogLevel(self) -> LogLevel:
    pass


class Debug(BaseError):
  @staticmethod
  def level():
    return ErrorLevel.DEBUG

  def getLogLevel(self) -> LogLevel:
    pass
