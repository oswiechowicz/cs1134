class Empty(Exception):
    pass

class BoostQueue():
    initialcap=5

    def __init__(self):
        self.data=[None]*BoostQueue.initialcap
        self.front=0
        self.n=0

    def __len__(self):
        return self.n;

    def is_empty(self):
        return self.n==0

    def enqueue(self,item):
        if self.n==len(self.data):
            self.resize(2*len(self.data))
        end_ind=(self.front+self.n)%len(self.data)
        self.data[end_ind]=item
        self.n+=1


    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        value=self.data[self.front]
        self.data[self.front]=None #set to none too free memory
        self.front=(self.front+1)%len(self.data)
        self.n-=1
        if (self.n<(len(self.data)//4)):
            self.resize(len(self.data))
        return value

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self.data[self.front]

    def boost(self,k):
        if self.is_empty():
            raise Empty('Queue is empty')
        elif k>self.n:
            last_item=self.data[self.n-1]
            self.data.insert(last_item,0)
            self.data.pop(self.n-1)

        else:
            first_part=self.data[:self.n-k]
            last_part=self.data[self.n-k:self.n-1]
            last_item=self.data[self.n-1]

            first_part.append(last_item)
            first_part.extend(last_part)

            self.data=first_part+self.data[self.n:len(self.data)]



    def resize(self,newcap):
        new_data=[None]*newcap
        old_ind=self.front
        for new_ind in range(self.n):
            new_data[new_ind]=self.data[old_ind]
            old_ind=(old_ind+1)

def main():
    q=BoostQueue()
    print(q.data)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.data)
    q.boost(2)
    print(q.data)

main()