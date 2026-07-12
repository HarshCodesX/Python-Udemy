chai_order = dict(type="Masala Chai", size="Large", sugar = 2)
# print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "water"
chai_recipe["tea_type"] = "black tea"

# print(f"Chai Recipe: {chai_recipe}")
# print(f"Chai base is {chai_recipe['base']} and tea type is {chai_recipe['tea_type']}")

del chai_recipe["tea_type"]
# print(f"Chai Recipe after deleting tea type: {chai_recipe}")

# print(f"Is sugar in the chai order? {'sugar' in chai_order}")
# print(f"Is sugar in the chai recipe? {'sugar' in chai_recipe}")

# print(f"Chai order keys: {chai_order.keys()}")
# print(f"Chai order values: {chai_order.values()}")
# print(f"Chai order items: {chai_order.items()}")

last_item = chai_order.popitem()
# print(f"Chai order after popping last item: {chai_order}")
# print(f"Last item popped from chai order: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
# print(f"Chai recipe after adding extra spices: {chai_recipe}")

chai_size = chai_order["size"]
# print(f"Chai size from order: {chai_size}")

# another way of doing the same thing as line 29, as it will throw error if we get something which is not present in the chai_order dictionary
note = chai_order.get("note", "no note present")
print(f"Customer note from order using get method: {note}")