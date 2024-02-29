import sys
import pytest


if __name__ == "__main__":
    if "-test" in sys.argv:
        pytest.main(__file__)
