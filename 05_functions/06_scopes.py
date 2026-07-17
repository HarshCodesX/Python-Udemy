# def serve_chai():
#     chai_type = "masala" # local scope
#     print(f"Inside function: {chai_type}")

# chai_type = "lemon"
# serve_chai()
# print(f"Outside function: {chai_type}")

# another example

def chai_counter():
    chai_order = "lemon" #Enclosing scope
    def print_order():
        chai_order = "ginger"
        print(f"Inner: {chai_order}")
    print_order()
    print(f"Outer: {chai_order}")

chai_order = "black tea"
chai_counter()
print(f"Global: {chai_order}")