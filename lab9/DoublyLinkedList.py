class DoublyLinkedList:
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
        self.header = self.Node()
        self.trailer = self.Node()
        self.size = 0
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size==0

    def first_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.header.next

    def last_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.trailer.prev

    def add_first(self,new_data):
        return self.add_after(self.header,new_data)

    def add_last(self,new_data):
        return self.add_after(self.trailer.prev, new_data)

    def add_after(self,node,new_data):
        pred=node
        succ=node.next
        new_node=DoublyLinkedList.Node(new_data,succ,pred)
        pred.next=new_node
        succ.prev=new_node
        self.size+=1
        return new_node

    def delete_first(self):
        if self.is_empty():
            raise Exception("list is empty")
        return self.delete_node(self.first_node())

    def delete_last(self):
        if self.is_empty():
            raise Exception("list is empty")
        return self.delete_node(self.last_node())

    def delete_node(self, node):
        pred=node.prev
        succ=node.next
        pred.next=succ
        succ.prev=pred
        data=node.data
        self.size-=1
        node.disconnect()
        return data

    def __iter__(self):
        if self.is_empty():
            return
        cursor=self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor=cursor.next

    def __repr__(self):
        return '[' + '<-->'.join((str(item)) + ']' for item in self) +"]"
        #lst=[str(item) for item in self]
        #return '[' + '<-->'.join(list) + ']'



lnk_lst1=DoublyLinkedList()
lnk_lst1.add_first(4)
lnk_lst1.add_first(2)
lnk_lst1.add_last(7)
lnk_lst1.add_last(3)
lnk_lst1.add_last([1,2,3])
print(lnk_lst1)