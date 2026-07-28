class OutOfIngredientsError(Exception):
    pass

def make_tea(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("Tea is ready")

make_tea(0,1)