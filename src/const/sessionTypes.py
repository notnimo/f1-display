"""

Fastf1 identifiers are "Q", "R", "FP1", "SQ", etc.
this file contains mapping from, and to strings for the codes
so that is never hardcoded in the project.

https://docs.fastf1.dev/events.html ("Session identifiers")
"""

from dataclasses import dataclass

# from src.exception.exception import InvalidSessionException


@dataclass(frozen=True, slots=True)
class SessionType:
    code: str
    full_name: str


# session options list
# code is the string for fastf1.get_session()
SESSION_TYPES: tuple[SessionType, ...] = (
    SessionType("FP1", "Practice 1"),
    SessionType("FP2", "Practice 2"),
    SessionType("FP3", "Practice 3"),
    SessionType("SS", "Sprint Shootout"),
    SessionType("SQ", "Sprint Qualifying"),
    SessionType("S", "Sprint"),
    SessionType("Q", "Qualifying"),
    SessionType("R", "Race"),
)

_BY_CODE: dict[str, SessionType] = {s.code: s for s in SESSION_TYPES}
_BY_FULL_NAME: dict[str, SessionType] = {s.full_name.upper(): s for s in SESSION_TYPES}

# sessions on every weekend
CONVENTIONAL_SESSIONS: tuple[str, ...] = ("FP1", "FP2", "FP3", "Q", "R")

# Extra sessions layered on top of CONVENTIONAL_SESSIONS depending on the
# `EventFormat` value FastF1 assigns each round in get_event_schedule().
#
#   'sprint'             - legacy 2021-2022 format. FastF1 itself stores
#                          that era's sprint race session under the full
#                          name "Sprint Qualifying", even though it
#                          functioned like today's "Sprint" session - a
#                          historical naming quirk documented in FastF1's
#                          own session-identifier notes, not a mistake
#                          here. The code is still SQ for that period.
#   'sprint_shootout'    - 2023 format: adds Sprint Shootout (SS) + Sprint (S)
#   'sprint_qualifying'  - current format: adds Sprint Qualifying (SQ) + Sprint (S)
SPRINT_EVENT_FORMATS: dict[str, tuple[str, ...]] = {
    "sprint": ("SQ",),
    "sprint_shootout": ("SS", "S"),
    "sprint_qualifying": ("SQ", "S"),
}


def is_valid_session(value: str) -> bool:
    """True if value is a recognised session code or full name (not case-sensitive)."""
    if not value:
        return False
    possible: str = value.strip().upper()
    return possible in _BY_CODE or possible in _BY_FULL_NAME


def normalize_session(value: str) -> str:
    """returns FastF1 code from user input.

    accepts either a short code ("q", "R") or a full name ("qualifying",
    "Sprint"), not case-sensitive
    """
    if not value:
        return ""
    #   raise InvalidSessionException("session_type is required")

    candidate: str = value.strip().upper()

    if candidate in _BY_CODE:
        return candidate
    if candidate in _BY_FULL_NAME:
        return _BY_FULL_NAME[candidate].code

    #   raise InvalidSessionException(f"'{value}' is not a recognised session type")
    return ""


def display_name(code: str) -> str:
    """returns full display name for a canonical code 'Q' -> 'Qualifying'."""
    session: SessionType | None = _BY_CODE.get((code or "").strip().upper())
    if session is None:
        return ""
    #    raise InvalidSessionException(f"'{code}' is not a recognised session type")
    return session.full_name


def sessions_for_event_format(event_format: str) -> tuple[str, ...]:
    """returns which session codes are selectable for a given weekend EventFormat.

    `event_format` is the value FastF1 puts in the schedule's EventFormat
    column ('conventional', 'sprint', 'sprint_shootout', 'sprint_qualifying',
    'testing').
    """
    extra: tuple[str, ...] = SPRINT_EVENT_FORMATS.get((event_format or "").strip().lower(), ())
    return CONVENTIONAL_SESSIONS + extra


if __name__ == "__main__":
    for session in SESSION_TYPES:
        print(f"{session.code:>4}  {session.full_name}")
