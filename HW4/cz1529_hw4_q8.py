def flat_list(nested_lst, low, high):
    if(low > high):
        return []
    out = []
    if(isinstance(nested_lst[low], int)):
        out.append(nested_lst[low])
    else:
        out += flat_list(nested_lst[low], 0, (len(nested_lst[low])-1))
    out += flat_list(nested_lst, low+1, high)
    return out

def main():
    lst=[[1,2],3,[4,[5,6,[7],8]]]
    print(flat_list(lst,0,2))
