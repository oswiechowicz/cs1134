def product_evens(lst):
    total=1
    n=0
    if (n>=len(lst)-1):
        return total

    else:
        if (lst[0]<n) and (lst[0]%2==0):
            total=lst[0]*total
            return product_evens(lst[n+1:])
        else:
            return product_evens(lst[n+1:])

def main():
    lst=[1,2,3,4,5,100,12,2]
    n=8
    print(product_evens(lst))

main()