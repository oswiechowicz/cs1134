from DoublyLinkedList import*

def sum_lnk_lst(lnk_lst):
    if lnk_lst.header.data==None:
        return 0
    else:
        rest=sum_lnk_lst(lnk_lst.next)
        return sum(rest+sum_lnk_lst(rest.next))


lnk_lst=DoublyLinkedList()
lnk_lst.add_last(1)
lnk_lst.add_last(2)
lnk_lst.add_last(3)
lnk_lst.add_last(4)
print(lnk_lst)
print(sum_lnk_lst(lnk_lst))