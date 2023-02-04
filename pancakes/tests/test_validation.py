import pytest

from q17 import solve

# List of test cases in the form [(input, output)]
# Ideally there should be 10 test cases
TEST_CASES = [
    ([5, 4, 3, 2, 1], [], 1),
    ([3, 2, 1], [2, 3, 2, 3, 2], 3),
]


@pytest.mark.parametrize("input1, input2 ,expected", TEST_CASES)
def test_validation(input1, input2, expected):
    assert solve(input1, input2) == expected
