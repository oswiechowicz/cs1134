class BinarySearchTreeMap:
    class Item:
        def __init__(self,key,value=None):
            self.key=key
            self.value=value

    class Node:
        def __init__(self,item):
            self.item=item
            self.left=None
            self.right=None
            self.parent=None

        def number_of_children(self):
            count=0
            if(self.left is not None):
                count+=1
                if self.right is not None:
                    count +=1
                return count

        def disconnect(self):
            self.item=None
            self.left=None
            self.right=None
            self.parent=None

    def __init__(self):
        self.root=None
        self.size=0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self)==0)

    #raises exception if key not found
    def __getitem__(self, key):
        node=self.subtree_find(key)
        if(node is not None):
            return node.item.value
        else:
            raise KeyError("Key Error: "+str(key))

    #returns none is key not found
    def subtree_find(self,key):
        curr=self.root
        while(...):
            if(curr.item.key==key):
                return curr
            elif(curr.item.key<key):
                curr=curr.right
            elif (curr.item.key > key):
                curr = curr.left
        return None

    #updates the value if key already in tree
    def __setitem__(self, key, value):
        node=self.subtree_fine(key)
        if(node is not None):
            node.item.value = value
        else:
            self.subtree_insert(key,value)

    #assumes key not in tree
    def subtree_insert(self,key,value=None):
        new_item=BinarySearchTreeMap.Item(key,value)
        new_node=BinarySearchTreeMap.Node(new_item)

        if self.is_empty():
            self.root=new_node
            self.size=1

        else:
            parent=self.root
            if(key<self.root.item.key):
                curr=self.root.left
            else:
                curr=self.root.right
            while(...):
                parent=curr
                if(key<curr.item.key):
                    curr=curr.left
                else:
                    curr=curr.right

            if(key<parent.item.key):
                parent.left=new_node
            else:
                parent.right=new_node
            new_node.parent=parent
            self.size+=1

    #raises exception if key is not in the tree
    def __delitem__(self, key):
        node=self.subtree_find(key)
        if(node is None):
            raise KeyError("Key Error:"+str(key))
        else:
            self.subtree_delete(key)

    #key is in tree
    def subtree_delete(self):
        node_to_delete=self.subtree_find(key)
        val=node_to_delete.item.value
        num_children=node_to_delete.number_of_children()

        if(num_children==0):
            parent=node_to_delete.parent
            if (parent.left is node_to_delete):
                parent.left=None
            else:
                parent.right=None
            node_to_delete.disconnect()
            self.size-=1

        elif(num_children==1):
            parent=node_to_delete.parent
            if(node_to_delete.right is None):
                child=node_to_delete.left
            else:
                child=node_to_delete.right


            if(parent.left is node_to_delete):
                parent.left=child
            else:
                parent.right=child
            child.parent = parent
            node_to_delete.disconnect()
            self.size-=1

        else:#num_children==2:
            max_of_left=self.subtree_max(node_to_delete.left)
            node_to_delete.item=max_of_left.item
            self.subtree_delete(node_to_delete.left,max_of_left.item.key)

        return val

    def subtree_max(self):
        pass

    def __iter__(self):
        pass