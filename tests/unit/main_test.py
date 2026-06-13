import pytest as pt
from hypothesis import example, given
from hypothesis import strategies as st

from notypehints import main


def test_main():
    assert main.main(b"OK") == "OK"
    assert main.main(b"NOT OK") == "NOT OK"
    assert main.main(b"\xff") == "NOT OK"
    assert main.main(b"bad") == "Error: Found forbidden word"
    assert main.main(b"x" * 1001) == "Error: Input too large"
    assert main.main(b"something bad here") == "Error: Found forbidden word"


@given(st.integers(18, 20))
def test_dummy_age_verifier(age):
    assert main.dummy_age_valid(age) == 1


@given(st.integers(0, 17))
@example(age=0).via("discovered failure")
def test_dummy_age_verifier_raises(age):
    with pt.raises(ValueError):
        main.dummy_age_valid(age)
