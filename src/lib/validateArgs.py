from src.const.driversList import getDriversList

from src.exception.exception import InvalidArgumentException, InvalidDriverIDException


def validateArgs(**args) -> bool:
  if not args["driver1"]:
    raise InvalidArgumentException("driver 1 is required")
  if not args["driver1"] >= 0 and not args["driver1"] < len(getDriversList()):
      raise InvalidDriverIDException("driver 1 is provided but inexistent")
  
  # check driver 1 with other args (was it on the grid if year is specified)

  if args["driver2"]:
    if not args["driver2"] >= 0 and not args["driver2"] < len(getDriversList()):
      raise InvalidDriverIDException("driver 2 is provided but inexistent")
    
    if args["driver2"] == args["driver1"]:
      raise InvalidArgumentException("driver 2 and driver 1 have the same value")
    
    # check driver 2 with other args (was it on the grid if year is specified)

  # check pertinence of round and year

  # check session type

  return True