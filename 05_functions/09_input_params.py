chai = "Ginger chai"
def prepare_chai(order):
    print("Preparing", chai)
# prepare_chai(chai)

# ANOTHER EXAMPLE

chai = [1, 2, 3]
def edit_chai(cup):
    cup[1] = 42
# edit_chai(chai)
# print(chai)

# ANOTHER EXAMPLE
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

# make_chai("black tea", "amul milk", "brown sugar") #positional arguments
# make_chai(tea = "Ginger", sugar = "brown sugar", milk = "amul toned") #keywords arguments

# ANOTHER EXAMPLE

def special_tea(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

# special_tea("Cinnamon", "Cardamom", sweetner = "Honey", foam = "Milk foam")

# ANOTHER EXAMPLE
# def chai_order(order = []):
#     order.append("Masala chai")
#     print(order)

def chai_order(order = None):
    if order is None:
        order = []
        order.append("Masala")
    print(order)

chai_order()
chai_order()
