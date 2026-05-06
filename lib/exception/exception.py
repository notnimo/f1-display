class GeneralF1DisplayException(BaseException):
  def __init__(self, message: str):
    self.message = message
    super().__init__(self.message)
  
class InvalidArgumentException(GeneralF1DisplayException):
  def __init__(self, message: str):
    super().__init__("Exception: Invalid Argument.\n  " + message)

class InvalidRaceException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__("Exception: Race Selected.\n    " + message)

class InvalidYearException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__("Exception: Invalid Year.\n    " + message)

class InvalidDriverIDException(InvalidArgumentException): 
  def __init__(self, message: str):
    super().__init__("Exception: Invalid Driver ID.\n    " +  message)

class InvalidSessionException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__("Exception: Invalid Session.\n    " + message)