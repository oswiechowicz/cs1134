import LinkedBinaryTree

def invert_binary_tree(root):
    if root.left is None and root.right is None:
        return None
    else:
        return invert_binary_tree(root.left),invert_binary_tree(root.right)=invert_binary_tree(root.right),invert_binary_tree(root.left)