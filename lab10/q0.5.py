from DoublyLinkedList import *

def prime_factorization(int):
    lnklst=DoublyLinkedList()
    for i in range(2,int):
        if int%i==0:
            lnklst.add_last(i)


    return lnklst

n=24
print(prime_factorization(n))
