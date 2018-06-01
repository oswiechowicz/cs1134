def binary_search(srt_lst,val,low,high):
    if low>high:
        return None
    else:
        mid=(low+high)//2
        if val==srt_lst[mid]:
            return mid
        elif val<=srt_lst[mid]:
            binary_search(srt_lst,val,low,mid)
        else:
            binary_search(srt_lst,val,mid+1,high)

def main():
    lst=[1,2,3,4,5,6,7,8,9,10]
    val=5
    print(binary_search(lst,11,0,9))

main()