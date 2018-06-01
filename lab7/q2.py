import ArrayStack

def eval_postfix_boolean_exp(boolean_exp_str):
    num=ArrayStack()
    operator=ArrayStack()
    boolsym={'>','<','<=',">=","==","!="}

    for item in boolean_exp_str:
        if item.isdigit():
            num.push(int(item))
        elif item in boolsym:
            other=num.pop()

def eval_postfix(expr):
    stack=ArrayStack()
    ops="<>|&"
    for token in expr.split():
        if token not in ops:
            stack.push(int(token))
        else:
            rhs=stack.pop()
            lhs=stack.pop()
            if token=="<":
                res=lhs<rhs
            elif token==">":
                res=lhs>rhs
            elif token=="|":
                res=lhs or rhs
            else:
                res=lhs and rhs
        stack.push(res)
    finalres=stack.pop()
    if not stack.empty():
        raise ValueError("Unbalanced expr")
    return finalres