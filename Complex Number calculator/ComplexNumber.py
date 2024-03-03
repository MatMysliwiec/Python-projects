class Complex_number:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {self.imag}i"


def add(a, b):
    real_part = a.real + b.real
    imag_part = a.imag + b.imag
    return Complex_number(real_part, imag_part)


def sub(a, b):
    real_part = a.real - b.real
    imag_part = a.imag - b.imag
    return Complex_number(real_part, imag_part)


def multi(a, b):
    real_part = a.real * b.real - a.imag * b.imag
    imag_part = a.real * b.imag + a.imag * b.real
    return Complex_number(real_part, imag_part)


def negate(a):
    return Complex_number(-a.real, -a.imag)


def invert(a):
    real_part = a.real / (a.real ** 2 + a.imag ** 2)
    imag_part = -a.imag / (a.real ** 2 + a.imag ** 2)
    return Complex_number(real_part, imag_part)


def div(a, b):
    real_part = a.real * b.real + a.imag * b.imag / (b.real ** 2 + b.imag ** 2)
    imag_part = a.imag * b.real - a.real * b.imag / (b.real ** 2 + b.imag ** 2)
    return Complex_number(real_part, imag_part)


def conjugate(a):
    return Complex_number(a.real, -a.imag)
