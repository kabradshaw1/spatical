import copy

class a:
    x: float
    y: float
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy

a1 = a(1,2)
a2 = a1
a3 = copy.copy(a1)

print("a1.x = ", a1.x)
a2.x = 10
print("a1.x = ", a1.x)
a3.x = 100
print("a1.x = ", a1.x)
