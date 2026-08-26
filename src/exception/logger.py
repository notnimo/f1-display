from enum import Enum


class LogLevel(Enum):
  FULL = 0
  SHORT = 1
  SILENT = 2


class ErrorLevel(Enum):
  WARNING = 0
  ERROR = 1
  DEBUG = 2


class DebugLogger:
  def __init__(self, strbuf: str, log_level: LogLevel = LogLevel.FULL):
    self._strbuf = strbuf
    self._log_level = log_level

  def set_log_level(self, log_level: LogLevel):
    self._log_level = log_level

  def log(self, message: str, level: LogLevel = LogLevel.FULL):
    if self._log_level == LogLevel.SILENT:
      return
    if self._log_level == LogLevel.SHORT and level == LogLevel.FULL:
      return
    print(f"{self._strbuf} {message}")


debug: DebugLogger = DebugLogger("F1 display debug > ")
