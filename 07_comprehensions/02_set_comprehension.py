favourite_tea = [
    "Masala tea",
    "Green tea",
    "Masala chai",
    "Lemon tea",
    "Green tea",
    "cardamom tea"
]

# find all the unique tea's
unique_tea = {tea for tea in favourite_tea}
lengthShortenThanTen = {tea for tea in favourite_tea if len(tea) < 10}

# print(unique_tea)
# print(lengthShortenThanTen)

# *************Another example ****************

recipes = {
    "Masala tea": ["ginger", "cardamom", "clove"],
    "Cardamom tea": ["cardamom", "milk"],
    "Spicy tea": ["ginger", "black pepper", "clove"]
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)