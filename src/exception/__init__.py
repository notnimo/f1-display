import sys

from src.exception.error import (
  GeneralF1DisplayException,
  WarningException,
)
from src.exception.functions import break_on_throw, expect, force_throw, set_log_level, throw_error
from src.exception.register import error_register


def _fatal_excepthook(exc_type, exc, tb):
  if isinstance(exc, GeneralF1DisplayException):
    try:
      error_register.register_error(exc)
    except GeneralF1DisplayException:
      pass
    return
  sys.__excepthook__(exc_type, exc, tb)


sys.excepthook = _fatal_excepthook

__all__ = [
  "GeneralF1DisplayException",
  "WarningException",
  "error_register",
  "throw_error",
  "force_throw",
  "set_log_level",
  "break_on_throw",
  "expect",
]
