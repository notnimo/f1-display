class GeneralF1DisplayException(BaseException):
  def __init__(self, message: str):
    self.message = message
    super().__init__(self.message)
  
class InvalidArgumentException(GeneralF1DisplayException):
  def __init__(self, message: str):
    super().__init__(message)

class InvalidRaceException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__(message)

class InvalidYearException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__(message)

class InvalidDriverIDException(InvalidArgumentException): 
  def __init__(self, message: str):
    super().__init__(message)

class InvalidSessionException(InvalidArgumentException):
  def __init__(self, message: str):
    super().__init__(message)

class RaceWithoutYearException(GeneralF1DisplayException):
  """"""
  def __init__(self, message: str):
    foo: str = "" + message # @TODO add std info to message
    super().__init__(foo)