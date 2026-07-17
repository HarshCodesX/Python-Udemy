staff = [("Amit", 16), ("Zara", 18), ("Raj", 15)]
for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to work")
        break
else:
    print(f"no one is eligible to work")