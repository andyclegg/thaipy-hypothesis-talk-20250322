from bad64 import my_b64_encode, my_b64_decode
from base64 import b64encode as stdlib_b64_encode

from hypothesis import given, strategies

# Traditional tests
def test_known_example():
    assert my_b64_encode(b'ABC') == b'QUJD'

def test_roundtrip():
    assert my_b64_decode(my_b64_encode(b'XYZ')) == b'XYZ'

def test_oracle():
    assert my_b64_encode(b'123') == stdlib_b64_encode(b'123')

# Hypothesis tests
@given(strategies.binary())
def test_roundtrip(x):
    assert my_b64_decode(my_b64_encode(x)) == x

@given(strategies.binary())
def test_oracle(x):
    assert my_b64_encode(x) == stdlib_b64_encode(x)

