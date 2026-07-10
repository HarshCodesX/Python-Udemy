is_boiling = True # 1, and False is 0
stir_count = 5
total_actions = stir_count + is_boiling # upcasting
print(f"Total actions: {total_actions}")

milk_present = 0 # False
print(f"Is there milk? {bool(milk_present)}")

water_hot = True
# tea_added = False
tea_added = True

can_serve = water_hot and tea_added
print(f"Can serve tea? {can_serve}")