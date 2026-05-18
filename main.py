import sys

from src.cli.argsHandle import handleArgs

def main(driver1, driver2=-1, year=-1, round_number=-1, session_type='R'):
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

  main(driver1=settings['driver1'], driver2=settings['driver2']if settings['driver2'] is not None else -1, year=settings['year'] if settings['year'] is not None else -1, round_number=settings['round'] if settings['round'] is not None else -1, session_type=settings['session_type'] if settings['session_type'] is not None else 'R')