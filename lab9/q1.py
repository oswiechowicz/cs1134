from DoublyLinkedList import*

class LinkedStack:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data=None
            self.next=None
            self.prev=None

    def __init__(self):
        self.lnk_stack=DoublyLinkedList()

#        self.header = self.Node()
#        self.trailer = self.Node()
#        self.size = 0
#        self.header.next = self.trailer
#        self.trailer.prev = self.header

    def __len__(self):
        return self.lnk_stack.size

    def is_empty(self):
        return self.lnk_stack.size==0

    def top(self):
        top=self.lnk_stack.last_node().data
        print(top)
#        if self.is_empty():
#            raise Exception("List is empty")
#        return self.trailer.prev

    def push(self,new_data):
        self.lnk_stack.add_last(new_data)
#        return self.add_after(self.trailer.prev, new_data)

    def pop(self):
        self.lnk_stack.delete_last()
#        if self.is_empty():
#            raise Exception("list is empty")
#        return self.delete_node(self.last_node())

    def __iter__(self):
        if self.is_empty():
            return
        cursor=self.lnk_stack.first_node()
        while(cursor is not self.lnk_stack.trailer):
            yield cursor.data
            cursor=cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"
        #lst=[str(item) for item in self]
        #return '[' + '<-->'.join(list) + ']'



def main():
    lst = LinkedStack()
    print(lst)
    lst.push(1)
    print(lst)
    lst.push(2)
    print(lst)
    lst.push(3)
    print(lst)
    lst.push(4)
    print(lst)
    lst.top()
    lst.pop()
    print(lst)

main()