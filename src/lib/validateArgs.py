import fastf1

from src.const.driversList import getDriverWithId, getDriversList
from src.exception.exception import InvalidArgumentException, InvalidDriverIDException, InvalidYearException


def _parse_driver_index(driver, label: str) -> int:
  # Convert driver input to integer index and confirm it is inside the driver list.
  try:
    driver_index = int(driver)
  except (TypeError, ValueError):
    raise InvalidDriverIDException(f"{label} must be an integer index")

  if driver_index < 0 or driver_index >= len(getDriversList()):
    raise InvalidDriverIDException(f"{label} is provided but inexistent")

  return driver_index


def _parse_optional_int(value, label: str):
  # Treat missing or sentinel values as unset, otherwise parse an integer.
  if value is None or value == "" or value == -1:
    return None

  try:
    return int(value)
  except (TypeError, ValueError):
    raise InvalidYearException(f"{label} must be an integer")


def _get_session_driver_names(year: int, round_number: int, session_type: str) -> set[str]:
  # Load the requested FastF1 session and return the driver full names present.
  session = fastf1.get_session(year, round_number, session_type)
  session.load(telemetry=False, weather=False)
  return {session.get_driver(driver_no)["FullName"] for driver_no in session.drivers}


def _driver_competed_in_session(driver_name: str, year: int, round_number: int, session_type: str) -> bool:
  # Check whether the driver took part in the specific session.
  try:
    return driver_name in _get_session_driver_names(year, round_number, session_type)
  except Exception as exc:
    raise InvalidArgumentException(f"could not validate session {year} round {round_number} {session_type}: {exc}")


def _driver_competed_in_year(driver_name: str, year: int, session_type: str) -> bool:
  # Search the full year schedule for at least one session with this driver.
  schedule = fastf1.get_event_schedule(year)
  if schedule.empty:
    raise InvalidYearException(f"no event schedule found for year {year}")

  for round_number in schedule["RoundNumber"].dropna().astype(int).unique():
    try:
      if driver_name in _get_session_driver_names(year, round_number, session_type):
        return True
    except Exception:
      continue

  return False


def validateArgs(**args) -> bool:
  # Validate required driver 1 and convert to a driver name.
  driver1 = args.get("driver1")
  if driver1 is None or driver1 == "":
    raise InvalidArgumentException("driver 1 is required")

  driver1_index = _parse_driver_index(driver1, "driver 1")
  driver1_name = getDriverWithId(driver1_index)

  # Validate optional driver 2 and ensure it is not the same as driver 1.
  driver2 = args.get("driver2")
  driver2_index = None
  driver2_name = None
  if driver2 is not None and driver2 != "":
    driver2_index = _parse_driver_index(driver2, "driver 2")
    if driver2_index == driver1_index:
      raise InvalidArgumentException("driver 2 and driver 1 have the same value")
    driver2_name = getDriverWithId(driver2_index)

  # Parse year/round/session arguments for session validation.
  year = _parse_optional_int(args.get("year"), "year")
  round_number = _parse_optional_int(args.get("round"), "round")
  session_type = str(args.get("session_type") or "R").upper()

  # If a year is provided, verify driver participation either by session or by season.
  if year is not None:
    if round_number is not None:
      if not _driver_competed_in_session(driver1_name, year, round_number, session_type):
        raise InvalidArgumentException(
          f"driver 1 ({driver1_name}) was not on the grid for {year} round {round_number} {session_type}"
        )
      if driver2_name and not _driver_competed_in_session(driver2_name, year, round_number, session_type):
        raise InvalidArgumentException(
          f"driver 2 ({driver2_name}) was not on the grid for {year} round {round_number} {session_type}"
        )
    else:
      if not _driver_competed_in_year(driver1_name, year, session_type):
        raise InvalidArgumentException(f"driver 1 ({driver1_name}) did not compete in {year}")
      if driver2_name and not _driver_competed_in_year(driver2_name, year, session_type):
        raise InvalidArgumentException(f"driver 2 ({driver2_name}) did not compete in {year}")

  return True
