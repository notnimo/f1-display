import sys

from src.cli.argsHandle import handleArgs

def main(driver1, driver2=None, year=None, round_number=None, session_type='R'):
  print("session confirm message") # @TODO TO CHANGE
  # loadWhatever(args)

  # enable cache

  # manipulate data

  # display data
  pass

if __name__ == "__main__":

  if '--help' in sys.argv:
    with open('src/lib/help', 'r') as f:
      print(f.read())
    sys.exit(0)

  settings: dict[str, int | bool] = handleArgs(args=sys.argv)

  main(driver1=settings['driver1'], driver2=settings['driver2'], year=settings['year'], round_number=settings['round_number'], session_type=settings['session_type'])