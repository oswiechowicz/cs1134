def total_sum(lst):
    total=0

    if not isinstance(lst,list):
        return lst

    else:
        for i in lst:
            total+=total_sum(i)
        return total

def main():
    lst=[[1,2],[3,[[4]],5],6]
    print(total_sum(lst))

main()
