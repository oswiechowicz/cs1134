import math

def e_approx(n):
    return sum([1/(math.factorial(i)) for i in range(n+1)])

def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n =", n, "Approximation:", approx_str)

