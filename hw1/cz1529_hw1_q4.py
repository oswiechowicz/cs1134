#part a
def partA():
    return [10**i for i in range(6)]

#partb
def partB():
    return [i*(i+1) for i in range(10)]

#part c
def partC():
    return [chr(i) for i in range(97,123)]

def main():
    print(partA())
    print(partB())
    print(partC())

main()