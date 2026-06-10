#!/usr/bin/env python3
import sys

from main import main

try:
    import atheris
except ImportError:
    atheris = None


def fuzz_main(data: bytes) -> None:
    try:
        result = main(data)
        assert isinstance(result, str)
    except Exception as e:
        raise RuntimeError(f"Unexpected exception in main: {e}")


def _main():
    print("Setting up Atheris fuzzy testing...")

    if atheris is None:
        print("Atheris is not available. Install it with: pip install atheris")
        print("Note: Atheris requires clang and libFuzzer to be installed.")
    else:
        atheris.Setup(sys.argv, fuzz_main)

        print("Starting fuzzy testing... Press Ctrl+C to stop.")
        atheris.Fuzz()


if __name__ == "__main__":
    _main()
