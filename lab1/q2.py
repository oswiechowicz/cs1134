lst=[2,3,5,6,8,8]
lst2=[lst[i] for i in range(len(lst)) if(i%2==0 and lst[i]%2==0) ]
print(lst2)