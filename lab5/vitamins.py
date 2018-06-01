def f(ls):
    if (len(ls) == 1):
        return ls[0]
    else:
        return ls[0] + f(ls[1:])

def main():
    lst=[1,2,3,4,5,6,7,8,9,10]
    n=4
    print(f(lst))

main()