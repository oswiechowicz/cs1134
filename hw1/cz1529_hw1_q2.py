def shift(lst,k):
    temp=0
    #if k=0 return orignal list
    if k==0:
        return lst
    else:
        while k>0:
            temp=lst[0]
            lst.pop(0)
            lst.append(temp)
            k-=1
        return lst

def shiftDirection(lst,k,str="left"):
    if str.lower()=="left":
        shift(lst,k)
    if str.lower()=="right":
        reversed(lst);
        shift(lst,k);
        reversed(lst);
    return lst;

def main():
    lst=[1,2,3,4,5,6]
    print(shift(lst,2))
    print(shiftDirection(lst, 2,"right"))
