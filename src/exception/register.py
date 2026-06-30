from src.exception.error import GeneralF1DisplayException
from src.exception.logger import ErrorLevel, LogLevel, debug


class ErrorSettings:
  def __init__(self, log_level: LogLevel = LogLevel.FULL, break_on_throw: bool = False):
    self.log_level = log_level
    self.break_on_throw = break_on_throw


class ErrorRegister:
  def __init__(self):
    self._error_states = {}
    self._history = []
    self._to_handle = []

  def _settings_for(self, error_class):
    if error_class not in self._error_states:
      self._error_states[error_class] = ErrorSettings()
    return self._error_states[error_class]

  def register_error(self, error: GeneralF1DisplayException):
    error_class = type(error)
    settings = self._settings_for(error_class)
    self._history.append(error)
    self._to_handle.append(error)

    if settings.log_level == LogLevel.FULL:
      debug.log(f"{error.__class__.__name__}: {error.msg()}")
    elif settings.log_level == LogLevel.SHORT:
      debug.log(error.__class__.__name__, LogLevel.SHORT)

    if settings.break_on_throw:
      raise error

    if error.level() == ErrorLevel.ERROR:
      raise error

  def set_log_level(self, error_class, log_level: LogLevel):
    self._settings_for(error_class).log_level = log_level

  def break_on_throw(self, error_class, enabled: bool = True):
    self._settings_for(error_class).break_on_throw = enabled

  def has_error(self) -> bool:
    return bool(self._to_handle)

  def fetch_error(self) -> GeneralF1DisplayException:
    if not self._to_handle:
      raise IndexError("No pending errors")
    return self._to_handle.pop()


error_register = ErrorRegister()
