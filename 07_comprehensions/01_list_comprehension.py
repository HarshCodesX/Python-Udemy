menu = [
    "Masala chai",
    "Iced lemon tea",
    "Green tea",
    "Iced peach tea",
    "Ginger tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
greaterThanFive = [item for item in menu if len(item) > 10]
print(iced_tea)
print(greaterThanFive)