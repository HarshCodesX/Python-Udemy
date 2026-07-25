class TeaOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"here is your {self.size} chai of {self.type} flavour"

order = TeaOrder("Ginger", "medium")
print(order.summary())

orderTwo = TeaOrder("Cardamom", "Large")
print(orderTwo.summary())