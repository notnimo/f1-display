import pytest

from src.exception import error_register, expect, throw_error
from src.exception.error import DebugMessage, Error, WarningException


class CustomTemplateError(Error):
    template = "{0} is invalid for {1}"

class InvalidArgumentException(Error):
    template = "Invalid argument: {0}"

class LogFiles(DebugMessage):
    template = "Log files: {0}"


def test_throw_error_records_and_retrieves_errors():
    error = InvalidArgumentException("bad input")

    with pytest.raises(InvalidArgumentException):
        throw_error(error)

    assert error_register.has_error()
    fetched = error_register.fetch_error()
    assert isinstance(fetched, InvalidArgumentException)
    assert fetched.msg().endswith("Invalid argument: bad input\033[0m")
    assert "Invalid argument: bad input" in fetched.msg()


def test_expect_raises_on_false_condition():
    with pytest.raises(InvalidArgumentException):
        expect(False, InvalidArgumentException("expected failure"))


def test_template_supports_multiple_arguments():
    error = CustomTemplateError("foo", "bar")
    assert "foo is invalid for bar" in error.msg()


def test_messages_are_colored_by_severity():
    error = InvalidArgumentException("bad input")
    warning = WarningException("watch out")
    debug = DebugMessage("trace")

    assert error.msg().startswith("\033[31m") and error.msg().endswith("\033[0m")
    assert warning.msg().startswith("\033[33m") and warning.msg().endswith("\033[0m")
    assert debug.msg() == "trace"

def test3():
    error = LogFiles(str(["file1.log", "file2.log"]))
    throw_error(error)


if __name__ == "__main__":
    test3()