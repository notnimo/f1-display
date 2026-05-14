from datetime import datetime, timezone
from questionary import Style, select, Choice
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress, SpinnerColumn, TextColumn
import sys
import os
import subprocess
import fastf1
import pandas as pd

def enable_cache():
  # Get cache location from settings
  cache_path = "/__pycache__"

  # Check if cache folder exists
  if not os.path.exists(cache_path):
    os.makedirs(cache_path)

  # Enable local cache
  fastf1.Cache.enable_cache(cache_path)


FPS = 25
DT = 1 / FPS

def get_race_weekends_by_year(year: int) -> list[dict[str, str | int | dict[str, str]]]:
  """Returns a list of race weekends for a given year."""
  enable_cache()
  schedule = fastf1.get_event_schedule(year)
  weekends = []
  for _, event in schedule.iterrows():
    if event.is_testing():
      continue

    session_dates = {}
    for i in range(1, 6):
      session_name = event.get(f"Session{i}")
      session_date = event.get(f"Session{i}Date")
      if session_name and pd.notna(session_date):
        session_dates[str(session_name)] = session_date.isoformat()

    weekends.append(
      {
        "round_number": event["RoundNumber"],
        "event_name": event["EventName"],
        "date": str(event["EventDate"].date()),
        "country": event["Country"],
        "type": event["EventFormat"],
        "session_dates": session_dates,
      }
    )
  return weekends

def cli_load() -> None:
  current_year = datetime.now(timezone.utc).year

  style = Style([
    ("pointer", "fg:#e10600 bold"),
    ("selected", "noinherit fg:#64eb34 bold"),
    ("highlighted", "fg:#e10600 bold"),
    ("answer", "fg:#64eb34 bold")
  ])

  console = Console()
  console.print(Markdown("# F1 Display CLI"))

  with open('src/cli/driversNum.csv', 'r') as f:
    driverNum: list[list[str | int]] = [[], []]
    print(list(f))
    for line in f:
      num, name = line.strip().split(',')
      for i, n in enumerate(num):
        num[i] = int(n)
      driverNum[0].append(num)
      driverNum[1].append(name)

  driverChoices = [Choice(title=driver, value=driverNum[0][i]) for i, driver in enumerate(driverNum[1])]

  #define flag variables
  driver1: str = None
  driver2: str = None
  year: int = None
  round_number: int = None
  session: str = None

  # choosing first driver
  driver1 = select("Choose the first driver", choices=driverChoices, qmark="🏎️ ", style=style).ask()

  # single or h2h?

    # second driver if h2h

  # all time or specific year?
  all_time = select("All time?", choices=[Choice(title="Yes", value=True), Choice(title="No", value=False)], qmark="⏰ ", style=style).ask()
  if all_time is None:
    sys.exit(0)
  elif not all_time:
    # choosing year
    years = [str(year) for year in range(current_year, 2009, -1)]
    year = select("Choose a year", choices=years, qmark="🗓️ ", style=style).ask()
    if not year:
      sys.exit(0)
    else:
      year = int(year)

    # if round specific, ask round
    isRoundSpecific = select("Round specific?", choices=[Choice(title="Yes", value=True), Choice(title="No", value=False)], qmark="🏎️ ", style=style).ask()
    if isRoundSpecific is None:
      sys.exit(0)
    elif isRoundSpecific:
      with Progress(
        SpinnerColumn(style="bold red"),
        TextColumn("[bold]Loading races…"),
        console=console,
        transient=True,
      ) as progress:
        progress.add_task("load", total=None)
        data = get_race_weekends_by_year(year)

      rounds = [Choice(title=f"{row['event_name']} ({row['date']})",value=row['round_number']) for row in data]
      round_number = select("Choose a round", choices=rounds, qmark="🌏", style=style).ask()
      if not round_number:
        sys.exit(0)

      # ask what to compare (qualifying, sprint qualifying, race, sprint) when round specific
      sessions = ["Qualifying", "Race"]
      for row in data:
        if row['round_number'] == round_number:
          if row['type'].find('sprint') != -1:
            sessions.insert(0, "Sprint Qualifying")
            sessions.insert(1, "Sprint")
      session = select("Choose a session", choices=sessions, qmark="🏁", style=style).ask()
      if not session:
        sys.exit(0)
    else:
      # ask what to compare (qualifying, sprint qualifying, race, sprint) when not round specific
      sessions = ["Qualifying", "Race"]
      session = select("Choose a session", choices=sessions, qmark="🏁", style=style).ask()
      if not session:
        sys.exit(0)
  else:
    # if all time, ask what to compare (qualifying sessions, races)
    sessions = ["Qualifying", "Race"]
    session = select("Choose a session", choices=sessions, qmark="🏁", style=style).ask()
    if not session:
      sys.exit(0)


  flag = None
  match session:
    case "Qualifying":
      flag = "--qualifying" 
    case "Sprint Qualifying":
      flag = "--sprint-qualifying"  
    case "Sprint":
      flag = "--sprint"

  # build command to run main.py with the selected options
  main_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'main.py'))
  cmd = [sys.executable, main_path]

  if year is not None:
    cmd += ["--year", str(year)]
  else:
    cmd.append("--all-time")
  if round_number is not None:
    cmd += ["--round", str(round_number)]
  if flag:
    cmd.append(flag)
  if "--verbose" in sys.argv:
    cmd.append("--verbose")
  subprocess.run(cmd)

if __name__ == "__main__":
  cli_load()