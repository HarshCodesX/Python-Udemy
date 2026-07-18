chai_type = "plain"
def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irani"
        print("Inner chai is:", chai_type)
    kitchen()

front_desk()
print("chai type is:", chai_type)