# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total left: {remaining_tea}")

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings 
print(f"milk per serving: {milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots # "//" eliminiates what comes after decimal point
print(f"tea bags per pot: {bags_per_pot}")

total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup # "%" gives remainder
print(f"leftover cardamom pods: {leftover_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor # "**" raises to the power
print(f"powerful flavour strength: {powerful_flavour}")