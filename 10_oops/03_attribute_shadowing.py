class Tea:
    temperature = "hot"
    strength = "strong"

special_tea = Tea()

special_tea.temperature = "Mild hot"
special_tea.cup_size = "medium"
print(f"temperature of special tea after change: {special_tea.temperature}")
print(f"cup size: {special_tea.cup_size}")
print(f"temperature of temperature attribute inside the class: {Tea.temperature}")

del special_tea.temperature
del special_tea.cup_size

print(f"after deleting cup attribute: {special_tea.cup_size}") # this will throw an error as it doesnt have any fall back value unlike temperature
print(f"temp after deletion: {special_tea.temperature}")