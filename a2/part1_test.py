from hypothesis import given
from hypothesis.strategies import integers, lists, sets
from a2_part1_q1_q2 import mystery_1a_nested, mystery_1a_flat, mystery_1b_nested, mystery_1b_flat, \
    mystery_2a_if, mystery_2a_no_if, mystery_2b_if, mystery_2b_no_if


@given(x=lists(integers()), y=lists(integers()))
def test_mystery_1a(x: list[int], y: list[int]) -> None:
    """mystery_1a test"""

    assert mystery_1a_nested(x, y) == mystery_1a_flat(x, y)


@given(x=integers(), y=sets(integers()))
def test_mystery_1b(x: int, y: set[int]) -> None:
    """mystery_1b test"""

    assert mystery_1b_nested(x, y) == mystery_1b_flat(x, y)


@given(x=integers(), y=integers())
def test_mystery_2a(x: int, y: int) -> None:
    """mystery_2a test"""

    assert mystery_2a_if(x, y) == mystery_2a_no_if(x, y)


@given(x=integers(), y=integers())
def test_mystery_2b(x: int, y: int) -> None:
    """mystery_2b test"""

    assert mystery_2b_if(x, y) == mystery_2b_no_if(x, y)

# @given(n=integers(), m=integers())
# def test_gcd(n: int, m: int) -> None:
#     """mystery_2b test"""
#
#     if n >= m:
#         assert gcd(n, m) == gcd_original(n, m)
#     else:
#         assert gcd(m, n) == gcd_original(m, n)
#
# @given(n=integers(1, 5000), m=integers(50000, 100000))
# def test_gcd(n: int, m: int) -> None:
#     """mystery_2b test"""
#
#     assert gcd(n, m) == gcd_original(n, m)



