from queue import Queue

from src.exception.error import Error


class ErrorRegister:
  def __init__(self):
    self._error_queue = Queue()

  def register_error(self, error: Error):
    pass