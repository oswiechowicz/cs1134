#change prev and succ/header and trailer for each node
from DoublyLinkedList import*

def reverse_list_change_elements_order(lnk_lst):
    temp
    cursor=lnk_lst.header
    while not cursor == None:
        cursor.prev,cursor.next=cursor.next,cursor.prev

    return lnk_lst

lnk_lst=DoublyLinkedList()

lnk_lst.add_last(1)
lnk_lst.add_last(2)
lnk_lst.add_last(3)
lnk_lst.add_last(4)
print(reverse_list_change_elements_order(lnk_lst))