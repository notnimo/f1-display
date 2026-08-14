import sys

from src.cli import isTuiNecessary
from src.utils.format_args import formatArgs

def main():
# format args
  args: list = sys.argv # get args
  args.pop(0) # delete script name from args

  args_dict: dict = formatArgs(args) # format args into dict

# launch the TUI interface or launch the session if flags are provided
# cli.request(driver, session, year, week, mode, output, export) so that even if its only missing one arg i can still launch tui
  if isTuiNecessary(args_dict)[0]:
    pass

# validate args

# get data

# get settings for plotting
# plot

# export/display

# args = cli.parse_args()
# if args.has_explicit_target():
#   request = cli.build_request(args)
# else:
#   request = tui.selector.run()
# data = fastf1_client.load(request)
# figure = plotting.render(data, request.mode)
# export.output(figure, request)
  pass

