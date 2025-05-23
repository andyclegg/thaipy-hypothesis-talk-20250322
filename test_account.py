from account import Account
import tempfile
from hypothesis import given, strategies

names = strategies.text(min_size=3)
balances = strategies.integers(min_value=0)

@given(name=names, balance=balances)
def test_account_store_load_roundtrip(name, balance):
    a = Account(name, balance)

    with tempfile.NamedTemporaryFile() as f:
        a.store(f.name)
        assert a == Account.load(f.name)

@given(name1=names, name2=names, balance1=balances, balance2=balances, transaction_amount=strategies.integers())
def test_transaction(name1, name2, balance1, balance2, transaction_amount):
    a1 = Account(name1, balance1)
    a2 = Account(name2, balance2)

    a1.transfer(a2, transaction_amount)

    # State invariants
    assert a1.balance >= 0
    assert a2.balance >= 0

