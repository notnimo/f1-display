from lib.exception.exception import RaceWithoutYearException


def handleArgs(args: list[str]) -> dict[str, int | bool]:
  settings: dict[str, int | bool] = {}

  settings["driver1"] = args[1] # first argument is the first driver to load

  if "--year" in args: # year flag; next argument is the year to load
    settings["isYear"] = True
    settings["year"] = args[args.index("--year") + 1]

    if "--race" in args: # race flag; next argument is the round number; can only be used if year flag is also used
      settings["isRace"] = True
      settings["race"] = args[args.index("--race") + 1]
    else:
      settings["isRace"] = False

  else:
    if "--race" in args: # throw error if race is used without year
      raise RaceWithoutYearException("cli call used --race without year flag. arguments: " + " ".join(args))
    settings["isYear"] = False

  if "--h2h" in args: # head to head flag; the next argument is the second driver
    settings["h2h"] = True
    settings["driver2"] = args[args.index("--h2h") + 1]
  else:
    settings["h2h"] = False

  return settings
