essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices_box = essential_spices | optional_spices # union of two sets
print(f"All spices box: {all_spices_box}")

common_spices = essential_spices & optional_spices # intersection of two sets
print(f"Common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices # difference of two sets
print(f"Spices only in essential: {only_in_essential}")

print(f"Is cloves present in essential spices? {"cloves" in essential_spices}")
print(f"Is cloves present in optional_spices? {"cloves" in optional_spices}")