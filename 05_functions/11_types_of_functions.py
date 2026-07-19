cups = 5
def pure_function(cups):
    return cups * 10

# print(pure_function(cups))

# Impure function
def impure_function(cup):
    global cups
    cups += cup
    return cups

# print(impure_function(4))
# print(cups)

# Recursive function
def recursive_function(n):
    if n == 0:
        return "all cups poured"
    print(f"tea poured in cup number {n}")
    return recursive_function(n-1)

# recursive_function(5)

# Lambda function

chai_types = ["light", "strong", "ginger", "strong"]
strong_chai = list(filter(lambda chai: chai == "strong", chai_types))
not_strong_chai = list(filter(lambda chai: chai != "strong", chai_types))
print(strong_chai)
print(not_strong_chai)