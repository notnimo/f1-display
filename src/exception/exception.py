import sys
import traceback


def _format_message(message: str) -> str:
  # Replace tab separators with aligned new lines for CLI output.
  return message.replace("\t", "\n    ")


def _deepest_exception(exc: BaseException) -> BaseException:
  deepest = exc
  while True:
    next_exc = deepest.__cause__ or deepest.__context__
    if not next_exc:
      break
    deepest = next_exc
  return deepest


def _trace_location(exc: BaseException) -> str:
  if exc.__traceback__ is None:
    return ""

  frames = traceback.extract_tb(exc.__traceback__)
  if not frames:
    return ""

  last = frames[-1]
  col = getattr(last, "colno", None) or getattr(last, "end_colno", None) or getattr(last, "col_offset", None)
  if col is not None:
    return f"{last.filename}:{last.lineno}:{col}"
  return f"{last.filename}:{last.lineno}"


def _fatal_excepthook(exc_type, exc_value, exc_traceback):
  if exc_value is None:
    return

  deepest = _deepest_exception(exc_value)
  location = _trace_location(deepest)
  text = _format_message(str(deepest))
  if location:
    text = f"{text}\n  at {location}"
  sys.stderr.write(f"\033[31m{text}\033[0m\n")
  sys.exit(1)


sys.excepthook = _fatal_excepthook


class GeneralF1DisplayException(BaseException):
  def __init__(self, message: str):
    self.message = message
    super().__init__(self.message)

  def __str__(self) -> str:
    return _format_message(self.message)
  
class InvalidArgumentException(GeneralF1DisplayException):
  def __init__(self, message: str):
    super().__init__("Exception: Invalid Argument.\t" + message + " see --help flag to mode of use")

class InvalidRaceException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__("Invalid Race Selected.\t" + message)

class InvalidYearException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__("Invalid Year Selected.\t" + message)

class InvalidDriverIDException(InvalidArgumentException): 
  def __init__(self, message: str):
    super().__init__("Invalid Driver ID Selected.\t" +  message)

class InvalidSessionException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__("Invalid Session Selected.\t" + message)