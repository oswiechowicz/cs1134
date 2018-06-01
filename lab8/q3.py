from arrayqueue import *

def total_sum(nested_lst):
    q=ArrayQueue()
    q2=ArrayQueue()
    sum=0

    for i in nested_lst:
        if not isinstance(i,list):
            q.enqueue(i)
        else:
            q2.enqueue(i)

    while q2:
        for j in q2.dequeue():
            sum+=j
            q2.enqueue(sum)

def main():
    lst=[[1,2],[3,[[4],5]],6]
    print(total_sum(lst))

main()
