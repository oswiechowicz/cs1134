class CompactString:

    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        ind = 0
        counter = 1
        while ind != len(orig_str)-1:
            if orig_str[ind] == orig_str[ind+1]:
                counter += 1
            else:
                self.data.add_last((orig_str[ind], counter))
                counter = 1
            ind += 1
        self.data.add_last((orig_str[ind], counter))

    def __add__(self, other):
        new_string = ""
        for i in self.data:
            new_string += i[0] * i[1]
        for i in other.data:
            new_string += i[0] * i[1]
        return CompactString(new_string)

    def __lt__(self, other):
        curr1 = self.data.first_node()
        curr2 = other.data.first_node()
        while curr1 is not self.data.trailer and curr2 is not other.data.trailer:
            if curr1.data[0] != curr2.data[0]:
                return curr1.data[0] < curr2.data[0]
            else:
                if curr1.data[1] > curr2.data[1]:
                    if curr2.next is other.data.trailer:
                        return False
                    return curr1.data[0] < curr2.next.data[0]
                elif curr1.data[1] < curr2.data[1]:
                    if curr1.next is self.data.trailer:
                        return True
                    return curr1.next.data[0] < curr2.data[0]
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next
        if curr1 is self.data.trailer and curr2 is not other.data.trailer:
            return True
        return False

    def __le__(self, other):
        curr1 = self.data.first_node()
        curr2 = other.data.first_node()
        while curr1 is not self.data.trailer and curr2 is not other.data.trailer:
            if curr1.data[0] != curr2.data[0]:
                return curr1.data[0] < curr2.data[0]
            else:
                if curr1.data[1] > curr2.data[1]:
                    if curr2.next is other.data.trailer:
                        return False
                    return curr1.data[0] < curr2.next.data[0]
                elif curr1.data[1] < curr2.data[1]:
                    if curr1.next is self.data.trailer:
                        return True
                    return curr1.next.data[0] < curr2.data[0]
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next
        if curr1 is self.data.trailer:
            return True
        return False

    def __gt__(self, other):
        curr1 = self.data.first_node()
        curr2 = other.data.first_node()
        while curr1 is not self.data.trailer and curr2 is not other.data.trailer:
            if curr1.data[0] != curr2.data[0]:
                return curr1.data[0] > curr2.data[0]
            else:
                if curr1.data[1] > curr2.data[1]:
                    if curr2.next is other.data.trailer:
                        return True
                    return curr1.data[0] > curr2.next.data[0]
                elif curr1.data[1] < curr2.data[1]:
                    if curr1.next is self.data.trailer:
                        return False
                    return curr1.next.data[0] > curr2.data[0]
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next
        if curr1 is not self.data.trailer:
            return True
        return False

    def __ge__(self, other):
        curr1 = self.data.first_node()
        curr2 = other.data.first_node()
        while curr1 is not self.data.trailer and curr2 is not other.data.trailer:
            if curr1.data[0] != curr2.data[0]:
                return curr1.data[0] > curr2.data[0]
            else:
                if curr1.data[1] > curr2.data[1]:
                    if curr2.next is other.data.trailer:
                        return True
                    return curr1.data[0] > curr2.next.data[0]
                elif curr1.data[1] < curr2.data[1]:
                    if curr1.next is self.data.trailer:
                        return False
                    return curr1.next.data[0] > curr2.data[0]
                else:
                    curr1 = curr1.next
                    curr2 = curr2.next
        if curr2 is other.data.trailer:
            return True
        return False

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)







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

