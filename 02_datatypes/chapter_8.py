ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients: {ingredients}")
ingredients.remove("milk")
print(f"Ingredients after removing milk: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"Chai ingredients after adding spices: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")
print(f"Chai ingredients after inserting black tea: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Chai ingredients after popping last added ingredient: {chai_ingredients}")
print(f"Last added ingredient: {last_added}")

# reverse the list
chai_ingredients.reverse()
print(f"Chai ingredients after reversing: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Sugar max level: {max(sugar_levels)}")
print(f"Sugar min level: {min(sugar_levels)}")