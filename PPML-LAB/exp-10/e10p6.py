class Obj:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return Obj(self.a + other.a)

    def display(self):
        print("sum is:", self.a)

a = Obj(10)
b = Obj(20)
c = a + b
c.display()
