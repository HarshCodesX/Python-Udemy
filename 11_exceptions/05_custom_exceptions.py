def brew_tea(flavor):
    if flavor not in ["masala", "ginger", "cardamom"]:
        raise ValueError("We dont have this tea in our flavors")
    print(f"brewing {flavor} tea")

brew_tea("lemon")