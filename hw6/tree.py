#binary tree
class Node:

    def __init__(self, data, left=None, right=None):
        self.data=data
        self.parent=None
        self.left=left
        if(left is not None):
            self.left.parent=self
        self.right=right
        if(right is not None):
            self.right.parent=self

