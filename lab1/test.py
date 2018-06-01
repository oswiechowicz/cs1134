def __add__(self, other):
    total = []
    temp = 0
    if len(self.coeff) > len(other.coeff):
        self.coeffs, other.coeffs = other.coeffs, self.coeffs

    self.coeffs = [0] * (len(other.coeffs) - len(self.coeffs)) + self.coeffs

    for i in range(len(self.coeffs)):
        temp = self.coeffs[i] + other.coeffs[i]
        total.append(temp)

    return total


self.s = self, ((self.coeffs[i]), "x^", ((len(self.coeffs) - i)))


def __mul__(self, other):
    total = []
    length = (len(self.coeffs) - 1) + (len(other.coeffs) - 1)
    print(length)
    print(len(self.coeffs) - 1)
    while length > -1:
        total.append(0)
        length -= 1
    return total