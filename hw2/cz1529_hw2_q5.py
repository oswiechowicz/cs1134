def split_parity(lst):
    for i in range(len(lst)-1):
        if lst[i]%2==0 and not lst[i+1]%2==0: #compares each element next to each other
            lst[i],lst[i+1]=lst[i+1],lst[i] #swaps if first element is even and second is odd
    return lst

def main():
    lst=[1,2,3,4,5,6,7,8,9]
    print(split_parity(lst))

main()