import ctypes
def make_array(n):
    return (n*ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data=make_array(1)
        self.n=0
        self.capacity=1

    def __repr__(self):
        string=[]
        for i in range(self.n):
            string.append(self.data[i])
        return str(string);

    def resize(self,newsize):
        new_arr=make_array(newsize)
        for ind in range(self.n):
            new_arr[ind]=self.data[ind]
        self.data=new_arr
        self.capacity=newsize

    def __len__(self):
        return self.n;

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def append(self,val):
        if (self.n)==(self.capacity):
            self.resize(self.n*2)
        self.data[self.n]=val
        self.n+=1

    def __getitem__(self, k):
        if not 0<=abs(k)<=self.n:
            raise IndexError("invalid index")
        if k<0:
            negk=self.n+k
            return self.data[negk]
        return self.data[k]

    def __setitem__(self, ind, val):
        if not 0<=abs(ind)<=self.n:
            raise IndexError("invalid index")
        if ind<0:
            negk=self.n+ind
            self.data[negk]=val
        self.data[ind]=val

#PART A INSERT
    def insert(self, ind, val):
        if (self.n==self.capacity):
            self.resize(self.n*2)
        if not 0<=ind<=self.n:
            raise IndexError("invalid index")
        self.append(val)
        for i in range(self.n-1,ind,-1):
            self.data[i-1],self.data[i]=self.data[i],self.data[i-1]


#PART B POP
    def pop(self):
        if self.n<=0:
            raise IndexError("empty list")
        temp=self.data[self.n-1]
        self.data[self.n-1]=None
        self.n-=1
        if self.n<=(self.capacity//4):
            self.capacity=self.capacity//2
        return temp

#EXTRA CREDIT
    def pop2(self,ind):
        if self.n<=0:
            raise IndexError("empty list")
        temp=self.data[ind]
        self.data[ind]=None #value and ind is equal to none

        for i in range(ind, self.n-1): #move None to end
            self.data[i],self.data[i+1]=self.data[i+1],self.data[i]

        self.n-=1
        if self.n<=(self.capacity//4):
            self.capacity=self.capacity//2
        return temp

def main():
    lst=MyList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.append(4)
    lst.append(5)
    print(lst)
    lst.insert(2,30)
    print(lst)

