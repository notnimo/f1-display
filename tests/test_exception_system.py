import pytest

from src.exception import error_register, expect, throw_error
from src.exception.error import InvalidArgumentException


def test_throw_error_records_and_retrieves_errors():
    error = InvalidArgumentException("bad input")

    with pytest.raises(InvalidArgumentException):
        throw_error(error)

    assert error_register.has_error()
    fetched = error_register.fetch_error()
    assert isinstance(fetched, InvalidArgumentException)
    assert fetched.msg() == "bad input"


def test_expect_raises_on_false_condition():
    with pytest.raises(InvalidArgumentException):
        expect(False, InvalidArgumentException("expected failure"))
