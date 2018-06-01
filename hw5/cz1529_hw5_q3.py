from ArrayDeque import *
from ArrayStack import *
from ArrayQueue import *


class MidStack:

    def __init__(self):
        self.stack = ArrayStack()
        self.deque = ArrayDeque()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, val):
        if self.n == 0:
            self.stack.push(val)
        else:
            if len(self.stack) <= len(self.deque):
                self.stack.push(self.deque.delete_first())
            self.deque.add_last(val)
        self.n += 1

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.deque.last()

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        value = self.deque.delete_last()
        if len(self.stack) > len(self.deque):
            self.deque.add_first(self.stack.pop())
        self.n -= 1
        return value

    def mid_push(self, elem):
        if len(self.stack) == len(self.deque):
            self.stack.push(elem)
        else:
            self.deque.add_first(elem)
        self.n += 1


