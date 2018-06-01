#change last and first
from DoublyLinkedList import*

def reverse_list_change_elements_order(lnk_lst):
    while not lnk_lst == None:
        first=lnk_lst.first_node()
        last=lnk_lst.last_node()
        first, last = lnk_lst.last_node(),lnk_lst.first_node()
        lnk_lst.delete_first()
        lnk_lst.delete_last()
        lnk_lst.add_last(last)
        lnk_lst.add_first(first)


    return lnk_lst

lnk_lst=DoublyLinkedList()
lnk_lst.add_last(1)
lnk_lst.add_last(2)
lnk_lst.add_last(3)
lnk_lst.add_last(4)
print(reverse_list_change_elements_order(lnk_lst))

#---answer

def reverse(lst):
    firstNode=lst.header.next
    cursor=firstNode
    lst.header.next=lst.trailer.prev
    while cursor.data is not None:
        cursor.next, cursor.prev=cursor.prev, cursor.next
        cursor=cursor.prev
    firstNode.next=cursor
    cursor.prev=firstNode