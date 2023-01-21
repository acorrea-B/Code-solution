class Complejo(complex):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        super(Complejo, self).__init__()

    def sum(self, b):
        return self + b

    def subtract(self, b):
        return self - b

    def multiply(self, b):
        return self * b

    def divide(self, b):
        return self / b

    def mod(self):
        return complex(abs(self), float(0))


A = Complejo(5, 6)
B = Complejo(1, 2)

print(A.mod())
