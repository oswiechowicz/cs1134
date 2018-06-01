def split_by_sign(lst, low, high):
    if(low > high):
        return []
    if(lst[low] < 0):
        return [lst[low]] + split_by_sign(lst, low+1, high)
    else:
        return split_by_sign(lst, low+1, high) + [lst[low]]

def main():
    lst=[5,-3,6,-9,2,4,0,-1,1]
    print(split_by_sign(lst,0,8))

    #UH the code doesn't work when 1 is at the end of the list. it puts 1 before 0...
