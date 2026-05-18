from src.exception.exception import InvalidArgumentException


def handleArgs(args: list[str]) -> dict[str, int | bool]:
  """Handles the command line arguments for the F1 Display CLI.
  Args:
    args: A list of command line arguments.
  Returns:
    A dictionary of settings to be used in the main function.
  Raises:
    InvalidArgumentException: If the arg list is too short"""
  
  if len(args) < 2:
    raise InvalidArgumentException("cli call must include at least one driver\targs:" + str(args))

  settings: dict[str, int | bool] = {}

  settings["driver1"] = args[2] # first argument is the first driver to load

  if "--year" in args: # year flag; next argument is the year to load
    settings["year"] = args[args.index("--year") + 1]
  else:
    settings["year"] = None

  if "--round" in args: # race flag; next argument is the round number; can only be used if year flag is also used
    settings["round"] = args[args.index("--round") + 1]
  else:
    settings["round"] = None

  if "--session" in args: # session flag; next argument is the session type (e.g. R, Q, S)
    settings["session_type"] = args[args.index("--session") + 1]
  else:
    settings["session_type"] = None

  if "--driver2" in args: # head to head flag; the next argument is the second driver
    settings["driver2"] = args[args.index("--driver2") + 1]
  else:
    settings["driver2"] = None

  return settings
