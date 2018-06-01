def is_height_balanced(bin_tree):
    return is_height_balanced_helper(bin_tree.root)[0]

def is_height_balanced_helper(curr_node):
    if curr_node.left is None and curr_node.right is None:
        return (True, 1)
    if curr_node.left is not None and curr_node.right is not None:
        left_height = is_height_balanced_helper(curr_node.left)
        right_height = is_height_balanced_helper(curr_node.right)
    elif curr_node.left is not None and curr_node.right is None:
        left_height = is_height_balanced_helper(curr_node.left)
        right_height = (True, 0)
    else:
        left_height = (True, 0)
        right_height = is_height_balanced_helper(curr_node.right)
    difference = max(left_height[1], right_height[1]) - min(left_height[1], right_height[1])
    if difference > 1 or not left_height[0] or not right_height[0]:
        return (False, max(left_height[1], right_height[1]) + 1)
    return (True, max(left_height[1], right_height[1]) + 1)



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
