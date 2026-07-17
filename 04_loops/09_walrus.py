# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not completely divisible, remainder is {remainder}")

# new syntax of writing the above code ##########################

# value = 13
# if (remainder := value % 5):
#     print(f"Not completely divisible, remainder is {remainder}")

# ###################################

# available_sizes = ["small", "medium", "large"]
# if (requested_size := input("Enter your cup size: ")) in available_sizes:
#     print(f"Preparing {requested_size} cup of tea")
# else:
#     print(f"Size is unavailable - {requested_size}")

# #########################################

flavors = ["masala", "ginger", "lemon", "mint"]
print(f"Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Flavor is unavailable - {flavor}")

print(f"You choose {flavor} chai")