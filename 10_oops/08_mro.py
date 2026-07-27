#Method Resolution Order (MRO)

class A:
    label = "A: Base class"

class B(A):
    label = "B: Coming from B class which is inherited from A"

class C(A):
    label = "C: class C, which has inherited class A"

class D(B, C):
    pass

cup = D()
print(cup.label)
print(D.__mro__)