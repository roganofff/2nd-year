import pytest
from treasure import find_path

test_matrix = (
    ([
        ['x', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', 't']
    ], {'E': 2, 'S': 2}),
    ([
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', 'x', 't', '0', '0'],
        ['0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ], {'E': 1}),
    ([
        ['t', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', 'x']
    ], {'W': 6, 'N': 6})
)

@pytest.mark.parametrize('matrix, expected', test_matrix)
def test_find_path(matrix: list, expected: dict):
    res = find_path(matrix)
    assert (
        all([res.count(cord) == expected[cord] for cord in expected.keys()]) \
            and set(res) == set(expected.keys())
    ), f'{res}, {expected}'