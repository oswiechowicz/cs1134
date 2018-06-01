class Integer:

    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in num_str:
            self.data.add_first(int(i))

    def __str__(self):
        num = ""
        for i in self.data:
            num += str(i)
        return num[::-1]

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        num = ""
        placeholder = 0
        cursor1 = self.data.first_node()
        cursor2 = other.data.first_node()
        while cursor1 is not self.data.trailer and cursor2 is not other.data.trailer:
            sum = cursor1.data + cursor2.data + placeholder
            if sum > 9:
                num += str(sum % 10)
                placeholder = 1
            else:
                num += str(sum)
                placeholder = 0
            cursor1 = cursor1.next
            cursor2 = cursor2.next
        if cursor1 is self.data.trailer:
            while cursor2 is not other.data.trailer:
                if placeholder != 0:
                    num += str(cursor2.data + placeholder)
                    cursor2 = cursor2.next
                else:
                    num += str(cursor2.data)
                    cursor2 = cursor2.next
        else:
            while cursor1 is not self.data.trailer:
                if placeholder != 0:
                    num += str(cursor1.data + placeholder)
                    cursor1 = cursor1.next
                else:
                    num += str(cursor1.data)
                    cursor1 = cursor1.next
        return Integer(num[::-1])

    def __mul__(self, other):
        multiplier = 0
        placeholder = 0
        lst = []
        if len(self.data) > len(other.data):
            for i in other.data:
                new_Integer = ""
                for k in range(multiplier):
                    new_Integer += "0"
                for j in self.data:
                    num = i * j + placeholder
                    if num > 9:
                        new_Integer += str(num % 10)
                        placeholder = int(num / 10)
                    else:
                        new_Integer += str(num)
                        placeholder = 0
                lst.append(Integer(new_Integer[::-1]))
                multiplier += 1
        else:
            for i in self.data:
                new_Integer = ""
                for k in range(multiplier):
                    new_Integer += "0"
                for j in other.data:
                    num = i * j + placeholder
                    if num > 9:
                        new_Integer += str(num % 10)
                        placeholder = int(num / 10)
                    else:
                        new_Integer += str(num)
                        placeholder = 0
                if placeholder != 0: new_Integer += str(placeholder)
                lst.append(Integer(new_Integer[::-1]))
                placeholder = 0
                multiplier += 1
        result = Integer("0")
        for i in lst:
            result += i
        return result





#IMPORT DOUBLY LINKED LIST
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Exception("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Exception("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"

