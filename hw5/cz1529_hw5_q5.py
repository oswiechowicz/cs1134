from ArrayDeque import *
from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    stack = ArrayStack()
    queue = ArrayQueue()
    n = 0
    for i in range(len(lst)):
        lst[i], lst[n] = lst[n], lst[i]
        for a in lst:
            stack.push(a)
        for j in range(1, len(lst)-1):
            for k in range(j+1, len(lst)):
                lst[j], lst[k] = lst[k], lst[j]
                for a in lst:
                    stack.push(a)
                lst[k], lst[j] = lst[j], lst[k]
        lst[i], lst[n] = lst[n], lst[i]
    while stack:
        temp = []
        for i in range(len(lst)):
            temp.append(stack.pop())
        temp = temp[::-1]
        queue.enqueue(temp)
    return queue


