def list_min(lst,low,high):
    if (low>=high):
        return lst[low]
    else:
        min=(list_min(lst,low+1,high))
        if lst[low]<min:
            return lst[low]
        else:
            return min

def main():
    lst = [1, 2, 3, 4, 5, 100, 12, 2]
    print(list_min(lst,0,7))
