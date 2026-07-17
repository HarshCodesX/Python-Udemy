flavours = ["Ginger", "Out of stock", "Lemon", "discontinued", "tulsi"]
for flavour in flavours:
    if flavour == "Out of stock":
        print(f"{flavour} is out of stock")
        continue
    if flavour == "discontinued":
        print(f"{flavour} is discontinued")
        break
    print(f"Preparing {flavour} tea")

print("Outside the loop")