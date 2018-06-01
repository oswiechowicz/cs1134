import DoublyLinkedList

def remove_all(lnk_lst,item):
    if(lnk_lst.is_empty()):
        return ...
    cursor=lnk_lst.first_node()
    while(cursor.next is not lnk_lst.trailer):
        if(item==cursor.data):
            next_node=cursor.next
            lnk_lst.delete_node(cursor)
            cursor=next_node
        else:
            cursor=cursor.next

def max_in_lnk_list(lnk_lst):
    if (lnk_lst.is_empty()):
        raise Exception("List is empty")
    return max in max_in_sub_lnk_list(lnk_lst,lnk_lst.first_node())
#    if len(lnk_lst)==1:
#        return lnk_lst.first_node().data
#    else:
#        max_in_lnk_list()

def max_in_sub_lnk_list(lnk_lst,sublist_head):
    if(sublist_head.next is lnk_lst.trailer):
        return sublist_head.data
    else:
        rest=max_in_sub_lnk_list(lnk_lst,sublist_head.next)
        return max(rest,sublist_head.data)

def max_in_list(lst):
    if(len(lst)==1):
        return lst[0]
    else:
        rest=max_in_list(lst[1:])
        return max(rest,lst[0])

def max_in_sublist(lst,low,high):
    pass

def average_compression(lnk_lst,k):
    if(lnk_lst.is_empty()):
        return Exception("List is empty")
    cursor=lnk_lst.first_node()
    while(...):
        curr_sum=0
        for i in range(k):
            curr_sum+=cursor.data
            next_node=cursor.next
            lnk_lst.delete_node(cursor)
            cursor=next_node
        curr_average=curr_sum/k
        lnk_lst.add_before(cursor,curr_average)