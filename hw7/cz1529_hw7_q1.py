def min_and_max(bin_tree):
    if bin_tree.root is None:
        raise EmptyTree("Tree is empty")
    else:
        return subtree_min_and_max(bin_tree, bin_tree.root)

def subtree_min_and_max(bin_tree, subtree_root):
    if subtree_root.left is None and subtree_root.right is None:
        return (subtree_root.data, subtree_root.data)
    current = subtree_root.data
    if subtree_root.left is not None and subtree_root.right is not None:
        left = subtree_min_and_max(bin_tree, subtree_root.left)
        right = subtree_min_and_max(bin_tree, subtree_root.right)
        return (min(left[0], right[0], current), max(left[1], right[1], current))
    elif subtree_root.left is None and subtree_root.right is not None:
        right = subtree_min_and_max(bin_tree, subtree_root.right)
        return (min(right[0], current), max(right[1], current))
    else:
        left = subtree_min_and_max(bin_tree, subtree_root.left)
        return (min(left[0], current), max(left[1], current))


#BinaryTreeClass
class EmptyCollection(Exception):
    pass

class EmptyTree(Exception):
    pass

class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self
            self.parent = None

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def subtree_count(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return left_count + right_count + 1

    def sum_tree(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if(subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return left_sum + right_sum + subtree_root.data

    def height(self):
        if (self.is_empty()):
            raise EmptyCollection("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    #assuming subtree_root is not empty
    def subtree_height(self, subtree_root):
        if((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif(subtree_root.left is None):
            return 1 + self.subtree_height(subtree_root.right)
        elif(subtree_root.right is None):
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)
