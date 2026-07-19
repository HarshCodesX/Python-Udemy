def make_chai():
    # return "Here is your chai/tea"
    print("Here is your chai/tea")
# returnVal = make_chai()
# print(returnVal)

# #######Another example ############
def ideal_chai():
    pass

# print(ideal_chai())

# #######Another example ############

def sold_cups():
    return 120

# total = sold_cups()
# print(total)

# #######Another example ############

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, we dont have more cups"
    return "Chai is ready"

# print(chai_status(0))
# print(chai_status(10))

# #######Another example ############

def chai_report():
    return 100, 20, 10 # sold, remianing 

sold, remaining, _ = chai_report()
print("Sold", sold, "cups and remaining cups left are", remaining)