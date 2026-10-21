import pytest
from cart import Cart, EmptyCartError
import sys

# @pytest.mark.skip(reason="결제 모듈 리팩터링 중")
# @pytest.mark.skipif(sys.platform == "win32", reason="리눅스 전용") 
# @pytest.mark.xfail(reason="알려진 버그, 티켓 #123")
def test_total_sums_items(cart): # 함수의 매개변수 이름과 fixture 이름(cart)을 일치시킴
    cart.add("book", 12000, 2)
    assert cart.total() == 24000


def test_empty_cart_raises(): 

    with pytest.raises(EmptyCartError):

        Cart().total()  # 빈 카트에서 total() 호출 시 EmptyCartError가 발생하는지 검증


# pytest는 기본적으로 test_*.py 또는 *_test.py 형태의 파일만 탐색
# pytest는 기본적으로 test method 이름에도 민감,  test_ 로 시작해야 인식.  

#@pytest.mark.xfail(reason="알려진 버그, 티켓 #123")
def test_negative_price_rejected():

    cart = Cart()

    with pytest.raises(ValueError, match="price must be"):

        cart.add("book", -100)