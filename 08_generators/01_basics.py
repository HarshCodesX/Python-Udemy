def serve_tea():
    yield "Cup 1: Masala tea"
    yield "Cup 2: Ginger tea"
    yield "Cup 3: Cardamom tea"

stall = serve_tea()
# print(stall)

# for tea in stall:
#     print(tea)

# *************Another Example*****************
def get_tea_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


#generator function
def get_tea_generator_func():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

tea = get_tea_generator_func()
print(tea)
print(next(tea))
print(next(tea))
print(next(tea))
# print(next(tea)) #will throw error