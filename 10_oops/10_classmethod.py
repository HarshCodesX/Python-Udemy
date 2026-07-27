class TeaOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"]
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)

class TeaUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large"]

print(TeaUtils.is_valid_size("medium"))

order1 = TeaOrder.from_dict({"tea_type": "ginger", "sweetness": "medium", "size": "small"})
order2 = TeaOrder.from_string("lemon-low-medium")
order3 = TeaOrder("masala", "low", "large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)