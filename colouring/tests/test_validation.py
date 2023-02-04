from textwrap import dedent
from typing import List, Set

import pytest

from q14 import solve

WHITE = False
BLACK = True

# List of test cases in the form [(input, output)]
TEST_CASES = [
    dedent(
        """\
        6 6
        1 2
        1 3
        2 4
        2 5
        3 4
        4 6
        """
    ),
]


@pytest.mark.parametrize("input", TEST_CASES)
def test_solver(input):
    assert is_correct(input, solve(input))


def _read_graph(input):
    # The first line is the number of vertices and edges
    lines = input.split("\n")
    first_line = lines.pop(0).strip()
    tokens = first_line.split(" ")
    n = int(tokens[0])
    k = int(tokens[1])
    # our graph will be an adjacency list
    g: List[Set] = [set() for i in range(n)]
    for edge in range(k):
        edge_line = lines.pop(0).strip()
        tokens = edge_line.split(" ")
        # vertices indexed starting from 0
        a = int(tokens[0]) - 1
        b = int(tokens[1]) - 1
        # this is an undirected graph
        g[a].add(b)
        g[b].add(a)

    return g


def is_correct(graph, colored: List[int]) -> bool:
    """Given a graph and a list of black nodes check if this
    solution is optimal"""
    g = _read_graph(graph)
    a = 1
    colour_a = WHITE
    colour_b = WHITE
    for neighbors in g:
        # check colors are different
        if a in colored:
            colour_a = BLACK
        else:
            colour_a = WHITE
        for b in neighbors:
            # careful there with the ids...
            if b + 1 in colored:
                colour_b = BLACK
            else:
                colour_b = WHITE
            if colour_a == colour_b:
                return False
        a = a + 1
    return True
