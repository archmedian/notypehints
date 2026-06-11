from notypehints import main


def test_main():
    assert main.main(b"OK") == "OK"
    assert main.main(b"NOT OK") == "NOT OK"
    assert main.main(b"\xff") == "NOT OK"
    assert main.main(b"bad") == "Error: Found forbidden word"
    assert main.main(b"x" * 1001) == "Error: Input too large"
    assert main.main(b"something bad here") == "Error: Found forbidden word"
