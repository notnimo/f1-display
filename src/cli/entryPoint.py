import sys

from main import main

# from src.cli.tuiSelector import tuiArgsSelect
# from src.cli.argsHandle import handleArgs

def entrypoint():
  if len(sys.argv) == 1:
#   call to tui args loader
#   tuiArgsSelect()
    return

  if '--help' in sys.argv:
    with open('src/lib/help', 'r') as f:
        print(f.read())
    sys.exit(0)

  settings = {} # handleArgs(args=sys.argv)

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