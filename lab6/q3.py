def pivot_element(lst):
    piv=lst[0]
    lst[:]=[i for i in lst if i<piv]
    return lst

def pivot_element2(lst):
    piv=lst[0]
    c1=0
    c2=len(lst)-1
    while c1 != c2:
        if lst[c1]>piv and lst[c2]<piv:
            lst[c1],lst[c2]=lst[c2],lst[c1]
        elif lst[c1]>piv:
            c2-=1
        else:
            c1+=1
    return lst

def pivot_element3(lst): #recursive
    pass

#LAB CODE
def sort_first(lst):
    first_bigger=1
    for i in range(1,len(lst)):
        if(lst[i]<lst[0]):
            lst[i],lst[first_bigger]=lst[first_bigger],lst[i]
            first_bigger+=1
    lst[first_bigger-1],lst[0]=lst=[0],lst[first_bigger]

#move numbers smaller to front and numbers bigger to the end
#same as piv_elem2 but it excludes the pivot number and
#then adds it at the end


def main():
    lst=[54,26,93,17,77,31,44,55,20]
    print(pivot_element(lst))
    lst=[54,26,93,17,77,31,44,55,20]
    print(pivot_element2(lst))

main()