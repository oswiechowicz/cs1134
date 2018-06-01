ops = "+-*/"
dic={}

def postfix_calculator(exp_str):

    result=""
    stack = ArrayStack()

    for token in exp_str.split():
        try:
            stack.push(int(token))
        except:
            if token in dic:
                stack.push(dic[token])

            elif token in ops:
                arg2 = stack.pop()
                arg1 = stack.pop()
                if token == '+':
                    res = arg1 + arg2
                elif token == '-':
                    res = arg1 - arg2
                elif token == '*':
                    res = arg1 * arg2
                else:
                    if arg2 == 0:
                        raise ZeroDivisionError("No division by 0")
                    res = arg1 / arg2
                stack.push(res)


            elif token == "=":
                result = stack.pop()
            else:
                stack.push(token)
    if result == "":
        return stack.pop()
    else:
        dic[result] = stack.pop()
        return result


#ALL THE CLASSES

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()


class ArrayQueue:
    INITIAL_CAPACITY = 10

    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
        self.data[back_ind] = elem
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self.data[self.front_ind]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0

class ArrayDeque:

    INITIAL_CAPACITY = 10

    def __init__(self):
        self.front_ind = 0
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0

    def __len__(self):
        return self.num_of_elems

    def is_empty(self):
        return (self.num_of_elems == 0)

    def add_first(self, elem):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        first = (self.front_ind - 1) % len(self.data)
        self.data[first] = elem
        self.front_ind = first
        self.num_of_elems += 1

    def add_last(self, e):
        if (self.num_of_elems == len(self.data)):
            self.resize(2 * self.num_of_elems)
        back = (self.front_ind + self.num_of_elems) % (len(self.data))
        self.data[back] = elem
        self.num_of_elems += 1

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        val = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % (len(self.data))
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("Deque is empty")
        back_ind = (self.front_ind + self.num_of_elems - 1) % (len(self.data))
        val = self.data[back_ind]
        self.data[back_ind] = None
        self.num_of_elems -= 1
        if (self.num_of_elems < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return val

    def first(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[self.front_ind]

    def last(self):
        if self.is_empty():
            raise Empty("Deque is empty")
        return self.data[(self.front_ind + self.num_of_elems - 1) % (len(self.data))]

    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0




def main():
    done = False
    while not done:
        inp = input("--> ")
        if inp != "done()":
            print(postfix_calculator(inp))
        else:
            done = True




main()

