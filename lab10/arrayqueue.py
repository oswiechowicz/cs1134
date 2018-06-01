class ArrayQueue:
    initialcap=5

    def __init__(self):
        self.data=[None]*ArrayQueue.initialcap
        self.front=0
        self.n=0

    def __len__(self):
        return self.n;

    def is_empty(self):
        return self.n==0

    def enqueue(self,item):
        end_ind=(self.front+self.n)%len(self.n)
        self.data[end_ind]=item
        self.n+=1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        value=self.data[self.front]
        self.data[self.front]=None #set to none too free memory
        self.front=(self.front+1)%len(self.data)
        self.n-=1
        if (self.n<(len(self.data)//4)):
            self.resize(len(self.data))
        return value

    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        return self.data[self.front]

    def resize(self,newcap):
        new_data=[None]*newcap
        old_ind=self.front
        for new_ind in range(self.n):
            new_data[new_ind]=self.data[old_ind]
            old_ind=(old_ind+1)



