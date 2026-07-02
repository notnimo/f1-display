from src.exception.logger import ErrorLevel


class GenericError(Exception):
  # Subclasses define a format string and receive any number of arguments.
  template = "{}"

  def __init__(self, *args):
    self._args = args
    self._message = self._format_message(*args)
    super().__init__(self._message)

  @classmethod
  def _format_message(cls, *args) -> str:
    if not args:
      return ""
    if cls.template == "{}":
      if len(args) == 1:
        return str(args[0])
      return " ".join(str(arg) for arg in args)
    try:
      return cls.template.format(*args)
    except (IndexError, KeyError, ValueError):
      return str(args[0]) if len(args) == 1 else " ".join(str(arg) for arg in args)

  def _apply_color(self, message: str) -> str:
    if self.level() == ErrorLevel.ERROR:
      return f"\033[31m{message}\033[0m"
    if self.level() == ErrorLevel.WARNING:
      return f"\033[33m{message}\033[0m"
    return message

  def msg(self) -> str:
    return self._apply_color(self._message)

  def what(self) -> str:
    return self.msg()

  def __str__(self) -> str:
    return self.msg()

  @staticmethod
  def level() -> ErrorLevel:
    return ErrorLevel.ERROR


class Error(GenericError):
  pass


class Warning(GenericError):
  @staticmethod
  def level() -> ErrorLevel:
    return ErrorLevel.WARNING
  

class DebugError(GenericError):
  @staticmethod
  def level() -> ErrorLevel:
    return ErrorLevel.DEBUG


# Compatibility aliases for the rest of the package.
GeneralF1DisplayException = GenericError
WarningException = Warning
DebugMessage = DebugError
