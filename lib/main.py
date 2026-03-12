import sys

def main(year, session):
  pass

if __name__ == "__main__":
  if "--help" in sys.argv:
    """ Help flag """
    pass
    sys.exit(0)

  if "-y" in sys.argv: 
    """ Year flag, e.g. -y 2023 """
    pass

  if "-h2h" in sys.argv:
    """ Head-to-head flag, e.g. -h2h 44 33 """
    pass

  if "-raceh2h" in sys.argv:
    """ Race head-to-head flag, e.g. -raceh2h 44 33 2023 Monza"""
    pass

  # add all possible flags

  