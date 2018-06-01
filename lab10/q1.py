from DoublyLinkedList import *

class Empty(Exception):
    pass

class BoostLink():

    def __init__(self):
        self.data=DoublyLinkedList()

    def __len__(self):
        return self.data.size

    def is_empty(self):
        return self.data.size==0

    def enqueue(self,item):
        self.data.add_last(item)

    def dequeue(self):
        if self.data.is_empty():
            raise Exception("Queue is empty")
        front=self.data.first_node().data
        self.data.delete_first()
        return front

    def first(self):
        if self.data.is_empty():
            raise Exception("Queue is empty")
        return self.data.first_node().data


    def boost(self,k):
        if self.is_empty():
            raise Empty('Queue is empty')

        elif k>=self.data.size:
            last_item=self.data.last_node().data
            self.data.add_first(last_item)
            self.data.delete_last()

        else:
            last_item = self.data.last_node().data
            curr_node=self.data.last_node()
            for cursor in range(k+1):
                curr_node=curr_node.prev

            self.data.add_after(curr_node,last_item)
            self.data.delete_last()

#            first_part=self.data[:self.n-k]
#            last_part=self.data[self.n-k:self.n-1]
#            last_item=self.data[self.n-1]

#            first_part.append(last_item)
#            first_part.extend(last_part)

#            self.data=first_part+self.data[self.n:len(self.data)]



def main():
    q=BoostLink()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.data)
    q.boost(6)
    print(q.data)
    q.boost(2)
    print(q.data)



#    q.boost(2)
#    print(q.data)

main()