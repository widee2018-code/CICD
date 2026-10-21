import pytest
from cart import Cart, EmptyCartError
import sys

@pytest.mark.parametrize("price, qty, expected",
[
(12000, 2, 24000), # 1번 케이스
(0, 5, 0), # 2번 케이스
(1000, 1, 1000), # 3번 케이스
],)

def test_total(cart, price, qty, expected):
    cart.add("item", price, qty)
    assert cart.total() == expected