class InvalidTeaError(Exception): pass
def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidTeaError("This tea is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} is {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("thank you")

bill("mint", 4)
bill("masala", "two")
bill("ginger", 5)