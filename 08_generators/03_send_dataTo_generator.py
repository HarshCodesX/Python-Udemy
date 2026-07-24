def tea_customer():
    print("which tea?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = tea_customer()
next(stall) #start the generator
stall.send("Masala tea")
stall.send("Lemon tea")