def chai_flavor(flavor = "masala"):
    """Return the flavor of chai"""
    chai="ginger"
    return flavor

# print(chai_flavor.__doc__)
# print(chai_flavor.__name__)

def generate_bill(chai = 0, cookie = 0):
    """
    Calculate the total bill for chai and cookie
    :param chai: Number of chai cups (10 rupee each)
    :param cookie: Number of cookie (15 rupee each)
    :return: (total amount, thank you message)
    """
    total = chai * 10 + cookie * 15
    return total, "Thank you for visiting!"

print(generate_bill.__doc__)