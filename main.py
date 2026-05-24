import sys

from src.cli.argsHandle import handleArgs
from src.const.driversList import getDriverWithId

def main(driver1, driver2=-1, year=-1, round_number=-1, session_type='R'):
  if driver2 == None:
    driver2 = -1
  if year == None:
    year = -1
  if round_number == None:
    round_number = -1
  if session_type == None:
    session_type = 'R'
  driver1_name = getDriverWithId(int(driver1))
  driver2_name = getDriverWithId(int(driver2)) if driver2 != -1 else None
  print(f"session confirmed for {driver1_name} {f'and {driver2_name}' if driver2_name else '\0'}{f' in ' if year != -1 or round_number != -1 else '\0'}{f'{year}' if year != -1 else '\0'}{f' round {round_number}' if round_number != -1 else '\0'}({session_type})") # @TODO TO CHANGE
  # validate args

  # enable cache

  # loadWhatever(args)

  # manipulate data

  # display data
  pass

if __name__ == "__main__":

  if '--help' in sys.argv:
    with open('src/lib/help', 'r') as f:
      print(f.read())
    sys.exit(0)

  settings: dict[str, int | bool] = handleArgs(args=sys.argv)
  print("Settings:", settings)

  main(driver1=settings['driver1'], driver2=settings['driver2'], year=settings['year'], round_number=settings['round'], session_type=settings['session_type'])