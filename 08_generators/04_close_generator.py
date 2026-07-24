#yield from and close in generators

def local_tea():
    yield "Masala tea"
    yield "Ginger tea"

def imported_tea():
    yield "Matcha tea"
    yield "Oolong tea"

def full_menu():
    yield from local_tea()
    yield from imported_tea()

# for tea in full_menu():
#     print(tea)

# **********Closeing a generator***********
def tea_stall():
    try:
        while True:
            order = yield "Waiting for tea order!"
            print(f"Preparing {order}")
    except:
        print("Stall closed, No more tea!")

stall = tea_stall()
print(next(stall))
stall.send("Lemon tea")
stall.close() #cleanup