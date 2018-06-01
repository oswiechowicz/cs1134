def shift(lst,k,str="left"):
    if k == 0:
        return lst

    if str.lower()=="left":
        while k > 0:
            temp = lst[0]
            lst.pop(0)
            lst.append(temp)
            k -= 1
        return lst

    elif str.lower()=="right":
        lst.reverse()
        while k > 0:
            temp = lst[0]
            lst.pop(0)
            lst.append(temp)
            k -= 1
        lst.reverse()
        return lst;

def main():
    lst=[1,2,3,4,5,6]
    print(shift(lst,2,"left"))
    lst2=[1,2,3,4,5,6]
    print(shift(lst2,2,"right"))
