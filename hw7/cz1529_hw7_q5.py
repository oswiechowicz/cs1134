#PART A
def create_expression_tree(prefix_exp_str):
    prefix_exp = prefix_exp_str.split(" ")
    for ind in range(len(prefix_exp)):
        try:
            prefix_exp[ind] = int(prefix_exp[ind])
        except:
            pass
    root_tuple = create_expression_tree_helper(prefix_exp, 0)
    return LinkedBinaryTree(root_tuple[0])


def create_expression_tree_helper(prefix_exp, start_pos):
    if isinstance(prefix_exp[start_pos], int):
        node = LinkedBinaryTree.Node(prefix_exp[start_pos])
        return (node, 1)
    else:
        left = create_expression_tree_helper(prefix_exp, start_pos + 1)
        right = create_expression_tree_helper(prefix_exp, start_pos + 1 + left[1])
        root = LinkedBinaryTree.Node(prefix_exp[start_pos], left[0], right[0])
        return (root, 1 + left[1] + right[1])


#PART B
def prefix_to_postfix(prefix_exp_str):
    tree = create_expression_tree(prefix_exp_str)
    return prefix_to_postfix_helper(tree.root)

def prefix_to_postfix_helper(curr_node):
    if curr_node.left is None and curr_node.right is None:
        return str(curr_node.data)
    left = prefix_to_postfix_helper(curr_node.left)
    right = prefix_to_postfix_helper(curr_node.right)
    root = curr_node.data
    return str(left + " " + right + " " + root)


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








    #PART A
    def create_expression_tree(prefix_exp_str):
        prefix_exp = prefix_exp_str.split(" ")
        for ind in range(len(prefix_exp)):
            try:
                prefix_exp[ind] = int(prefix_exp[ind])
            except:
                pass
        root_tuple = create_expression_tree_helper(prefix_exp, 0)
        return LinkedBinaryTree(root_tuple[0])


    def create_expression_tree_helper(prefix_exp, start_pos):
        if isinstance(prefix_exp[start_pos], int):
            node = LinkedBinaryTree.Node(prefix_exp[start_pos])
            return (node, 1)
        else:
            left = create_expression_tree_helper(prefix_exp, start_pos + 1)
            right = create_expression_tree_helper(prefix_exp, start_pos + 1 + left[1])
            root = LinkedBinaryTree.Node(prefix_exp[start_pos], left[0], right[0])
            return (root, 1 + left[1] + right[1])


    #PART B
    def prefix_to_postfix(prefix_exp_str):
        tree = create_expression_tree(prefix_exp_str)
        return prefix_to_postfix_helper(tree.root)

    def prefix_to_postfix_helper(curr_node):
        if curr_node.left is None and curr_node.right is None:
            return str(curr_node.data)
        left = prefix_to_postfix_helper(curr_node.left)
        right = prefix_to_postfix_helper(curr_node.right)
        root = curr_node.data
        return str(left + " " + right + " " + root)
