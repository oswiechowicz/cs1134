def find_lst_max(lst):
    n=0
    if (n>=(len(lst)-1)):
        return lst[n]
    else:
        max=(find_lst_max(lst[n+1:]))
        if lst[0]>max:
            return lst[0]
        else:
            return max

def main():
    lst = [1, 2, 3, 4, 5, 100, 12, 2]
    n = 8
    print(find_lst_max(lst))

main()

#notes
#if first value less than second, take out first
#elif lst[0]<lst[1] return find_max(lst[1:]
#elif lst[-1]<lst[-2] return find_max(lst[:-1]

#return max(lst[0],find_max(lst[1:]))