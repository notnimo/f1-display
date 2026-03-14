import sys
from lib.argsHandle import handleArgs

def main(year=None, session=None):
  print("session confirm message") # @TODO TO CHANGE
  # loadWhatever(args)

  # enable cache

  # manipulate data

  # display data
  pass

if __name__ == "__main__":
  settings: dict[str, int | bool] = handleArgs(sys.argv)
