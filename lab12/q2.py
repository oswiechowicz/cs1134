from binarysearchtree import *

def is_bst(binary_tree):
    return is_bst_helper(binary_tree.root)[0]


def is_bst_helper(curr_root):
    if curr_root==None:
        return True
    elif curr_root.data<min or curr_root.data >max:
        return False

    return is_bst(curr_root.left)


#answer
def isValid(root):
    if not curr.left and not curr.right:
        return (true, curr.item.key,curr.item.key)

    max.left=max_right=min_left=min_right=None



