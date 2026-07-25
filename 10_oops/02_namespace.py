class Tea:
    origin = "India"

# print(Tea.origin)
Tea.is_hot = True
print(f"Tea class property: {Tea.is_hot}")

# Creating objects from class Tea

ginger_tea = Tea()
ginger_tea.is_hot = False
ginger_tea.flavour = "ginger"
print(f"Tea type is: {ginger_tea.origin}")
print(f"hot or not: {ginger_tea.is_hot}")
print(f"flavour is: {ginger_tea.flavour}")
