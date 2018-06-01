from DoublyLinkedList import*

class LeakyStack:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data=None
            self.next=None
            self.prev=None

    def __init__(self,max_num):
        self.leakystack=DoublyLinkedList()
        self.cap=max_num

    def __len__(self):
        return self.leakystack.size

    def is_empty(self):
        return self.leakystack.size==0

    def top(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.leakystack.trailer.prev

    def push(self,new_data):
        if self.leakystack.size==self.cap:
            self.leakystack.delete_first()
            self.leakystack.add_last(new_data)
        else:
            return self.leakystack.add_after(self.leakystack.trailer.prev, new_data)

    def pop(self):
        if self.is_empty():
            raise Exception("list is empty")
        return self.leakystack.delete_node(self.leakystack.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        cursor=self.leakystack.first_node()
        while(cursor is not self.leakystack.trailer):
            yield cursor.data
            cursor=cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"
        #lst=[str(item) for item in self]
        #return '[' + '<-->'.join(list) + ']'



leakstack=LeakyStack(4)
leakstack.push(1)
print(leakstack)
leakstack.push(2)
print(leakstack)
leakstack.push(3)
print(leakstack)
leakstack.push(4)
print(leakstack)
leakstack.push(5)
print(leakstack)

