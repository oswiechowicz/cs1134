import LinkedBinaryTree

def eval_exp(exp_tree):
    if(exp_tree.is_empty()):
        raise Exception("Tree is empty")
    return subtree_eval_exp(exp_tree.root)

def subtree_eval_exp(curr_root):
    if(isinstance(curr_root.data,int)):
        return curr_root.data
    else:
        l_val=subtree_eval_exp(curr_root.left)
        r_val=subtree_eval_exp(curr_root.right)
        if(curr_root.data=="+"):
            return l_val+r_val
        elif(curr_root.data=="-"):
            return l_val-r_val
        if(curr_root.data=="*"):
            return l_val*r_val
        if(curr_root.data=="/"):
            return l_val/r_val
        else:
            raise Exception("unsupported operation: "+str(curr_root.data))


