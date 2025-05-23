import dataclasses, json, os

@dataclasses.dataclass
class Account:
    name: str
    balance: int = 0

    def store(self, fn):
        with open(fn, 'at') as f:
            json.dump({"name": self.name, "balance": self.balance}, f)

    @staticmethod
    def load(fn):
        with open(fn, 'rt') as f:
            data = json.load(f)
            return Account(data.get("name", ""), data.get("balance", 0))

    def transfer(self, other, update):
        # We don't allow a negative balance
        if self.balance >= update:
            self.balance -= update
            other.balance += update
