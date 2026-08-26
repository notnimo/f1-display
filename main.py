import sys

from cli.rtemp.argsHandle import handleArgs

from const.rtemp.driversList import getDriverWithId

from lib.rtemp.validateArgs import validateArgs

def main(driver1=None, driver2=None, year=None, round_number=None, session_type=None):
  validateArgs(driver1=driver1, driver2=driver2, year=year, round=round_number, session_type=session_type)

  driver1_name = getDriverWithId(int(driver1))
  driver2_name = getDriverWithId(int(driver2)) if driver2 else None
  print(f"session confirmed for {driver1_name} {f'and {driver2_name}' if driver2_name else '\0'}{f' in ' if year or round_number else '\0'}{f'{year}' if year else '\0'}{f' round {round_number}' if round_number else '\0'}({session_type})")
  print("provided arguments are valid, proceeding with data loading")

  # enable cache

  # loadWhatever(args)

  # manipulate data

  # display data

if __name__ == "__main__":

  if '--help' in sys.argv:
    with open('src/lib/help', 'r') as f:
      print(f.read())
    sys.exit(0)

  settings: dict[str, int | bool] = handleArgs(args=sys.argv)
#  print("Settings:", settings)

  call_args = {
    "driver1": settings["driver1"],
    "session_type": settings["session_type"],
  }
  if settings["driver2"] is not None:
    call_args["driver2"] = settings["driver2"]
  if settings["year"] is not None:
    call_args["year"] = settings["year"]
  if settings["round"] is not None:
    call_args["round_number"] = settings["round"]

  main(**call_args)