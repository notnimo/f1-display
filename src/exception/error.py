from abc import ABC, abstractmethod

from src.exception.logger import ErrorLevel


class GeneralF1DisplayException(ABC, Exception):
  def __init__(self, *args):
    self._message = self._format_message(*args)
    super().__init__(self._message)

  @staticmethod
  def _format_message(*args) -> str:
    if not args:
      return ""
    if len(args) == 1:
      return str(args[0])
    return " ".join(str(arg) for arg in args)

  @abstractmethod
  def msg(self) -> str:
    pass

  def what(self) -> str:
    return self.msg()

  def __str__(self) -> str:
    return self.msg()

  @staticmethod
  def level() -> ErrorLevel:
    return ErrorLevel.ERROR


class WarningException(GeneralF1DisplayException):
  @staticmethod
  def level() -> ErrorLevel:
    return ErrorLevel.WARNING


class InvalidArgumentException(GeneralF1DisplayException):
  def msg(self) -> str:
    return self._message


class InvalidYearException(GeneralF1DisplayException):
  def msg(self) -> str:
    return self._message


class InvalidDriverIDException(GeneralF1DisplayException):
  def msg(self) -> str:
    return self._message


class InvalidSessionException(GeneralF1DisplayException):
  def msg(self) -> str:
    return self._message
