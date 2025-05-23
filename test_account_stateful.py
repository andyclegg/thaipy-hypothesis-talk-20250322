from account import Account
from hypothesis import given, strategies as st, assume

from hypothesis.stateful import RuleBasedStateMachine, Bundle, rule

names=st.text(min_size=3)
balances=st.integers(min_value=0)

class AccountSimulator(RuleBasedStateMachine):
    accounts = Bundle("accounts")

    @rule(target=accounts, name=names, balance=balances)
    def create_account(self, name, balance):
        return Account(name, balance)

    @rule(a1=accounts, a2=accounts, amount=st.integers())
    def transfer(self, a1, a2, amount):
        assume(a1 != a2)
        a1.transfer(a2, amount)

    @rule(t=accounts)
    def debt_not_allowed(self, t):
        # This is an example of an Invariant
        assert t.balance >= 0

TestAccountSimulator = AccountSimulator.TestCase
