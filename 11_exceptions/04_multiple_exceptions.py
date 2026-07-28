def process_order(item, quantity):
    try:
        price = {"ginger": 20}[item]
        cost = price * quantity
        print(f"Total cost is: {cost}")
    except KeyError:
        print(f"Sorry that tea is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("cardamom", 2)
process_order("ginger", 3)