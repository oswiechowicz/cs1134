def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2, None, None, True)

def merge_sublists(lst1, lst2, curr1, curr2, checkEmpty):
    if checkEmpty:
        if len(lst1) == 0:
            return lst2
        elif len(lst2) == 0:
            return lst1
        else:
            curr1 = lst1.first_node()
            curr2 = lst2.first_node()
    new_lst = DoublyLinkedList()
    if curr1 is lst1.trailer:
        while curr2 is not lst2.trailer:
            new_lst.add_last(curr2.data)
            curr2 = curr2.next
        return new_lst
    if curr2 is lst2.trailer:
        while curr1 is not lst1.trailer:
            new_lst.add_last(curr1.data)
            curr1 = curr1.next
        return new_lst
    if curr1.data < curr2.data:
        new_lst.add_last(curr1.data)
        temp_lst = merge_sublists(lst1, lst2, curr1.next, curr2, False)
        new_lst.last_node().next = temp_lst.first_node()
        temp_lst.first_node().prev = new_lst.last_node()
        new_lst.trailer.prev = temp_lst.last_node()
        temp_lst.last_node().next = new_lst.trailer
    else:
        new_lst.add_last(curr2.data)
        temp_lst = merge_sublists(lst1, lst2, curr1, curr2.next, False)
        new_lst.last_node().next = temp_lst.first_node()
        temp_lst.first_node().prev = new_lst.last_node()
        new_lst.trailer.prev = temp_lst.last_node()
        temp_lst.last_node().next = new_lst.trailer
    return new_lst



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

