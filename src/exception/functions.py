from src.exception.error import GeneralF1DisplayException
from src.exception.logger import LogLevel
from src.exception.register import error_register


def throw_error(error: GeneralF1DisplayException):
  error_register.register_error(error)


def force_throw(error: GeneralF1DisplayException):
  error_register.register_error(error)


def set_log_level(error_class, log_level: LogLevel):
  error_register.set_log_level(error_class, log_level)


def break_on_throw(error_class, enabled: bool = True):
  error_register.break_on_throw(error_class, enabled)


def expect(condition: bool, error: GeneralF1DisplayException):
  if not condition:
    throw_error(error)
