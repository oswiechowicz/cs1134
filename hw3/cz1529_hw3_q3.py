def find_duplicates(lst):
    dic={} #create dictionary holding nums and how may times it appears
    dups=[]
    for i in range(len(lst)):
        item=lst[i]
        if item in dic:
            dic[lst[i]]+=1 #increase value if appears again
        else:
            dic[lst[i]]=1
    for k,v in dic.items(): #return all items that appeared more than once
        if v>1:
            dups.append(k)
    return dups


def main():
    lst=[2,4,4,1,2]
    print(find_duplicates(lst))


main()
