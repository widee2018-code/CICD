import pytest
from cart import Cart, EmptyCartError
import sys


# scope="session" 으로 둔 상태에서 테스트를 두 개 만듭니다
def test_first(cart):
    cart.add("book", 1000)
    assert len(cart.items) == 1

def test_second(cart):
    assert len(cart.items) == 0 # 새 장바구니를 기대

    