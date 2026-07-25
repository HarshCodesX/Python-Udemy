class Tea:
    pass


class TeaTime:
    pass

print(type(Tea))

ginger_tea = Tea()
print(type(ginger_tea))
print(type(ginger_tea) is Tea)
print(type(ginger_tea) is TeaTime)