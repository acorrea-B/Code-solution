class Complejo(complex):
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        super(Complejo).__init__()

    def __round__(self, complex):
        return Complejo(round(complex.real, 2), round(complex.imag, 2))

    def sum(self, b):
        return self.__round__(self + b)

    def subtract(self, b):
        return self.__round__(self - b)

    def multiply(self, b):
        return self.__round__(self * b)

    def divide(self, b):
        return self.__round__(self / b)

    def mod(self):
        return self.__round__(complex(abs(self)))
