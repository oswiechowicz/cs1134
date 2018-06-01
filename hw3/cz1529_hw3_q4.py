def remove_all(lst,value):
    lst[:]=[i for i in lst if i!=value]  #does list comprehension but the slicing mutates the list rather creating new one

def main():
    lst=[1,2,3,4,1,6,1,4,2,4]
    print(remove_all(lst,4))
    print(lst)
