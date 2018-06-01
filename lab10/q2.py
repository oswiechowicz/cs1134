from DoublyLinkedList import *

def flatten_link_lst(lnk_lst):
    new_lst=DoublyLinkedList()
    if len(lnk_lst)==1:
        return lnk_lst
    else:
        if isinstance(lnk_lst.first_node(),DoublyLinkedList()):
            flatten_link_lst(lnk_lst.first_node())
            for i in lnk_lst.len():
                if curr_node

    return rest+new_lst

#answer
def flattenlist(lnk_lst):
    result=DoublyLinkedList()
    curr=lnk_lst.first_node()
    while curr is not lnk_lst.trailer:
        if isinstance(curr.data,DoublyLinkedList()):
            for elem in flatten_link_lst(curr.data):
                result.add_last(elem)
        else:
            result.add_last(curr.data)
        curr=curr.next
    return result