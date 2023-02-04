from textwrap import dedent

import pytest

from q08 import solve

# List of test cases in the form [(input, output)]
TEST_CASES = [
    (
        dedent(
            """\
        4
        1 0 1 0
        0 0 0 0
        1 1 1 1
        0 1 0 1
        """
        ),
        "OK",
    ),
    (
        dedent(
            """\
        4
        1 0 1 0
        0 0 1 0
        1 1 1 1
        0 1 0 1
        """
        ),
        "Change bit (2,3)",
    ),
]


@pytest.mark.parametrize("input,expected", TEST_CASES)
def test_solver(input, expected):
    assert solve(input) == expected
