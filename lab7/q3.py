import ArrayStack

def convert_infix_exp_to_postfix(infix_exp_str):
    output=""
    num = ArrayStack()
    operator = ArrayStack()
    symb = {'-':2,'+':2,'/':3,'*':3,'(':1} #symbols have priorities

    for item in infix_exp_str:
        if item.isdigit():
            num.push(int(item))
        elif item in symb:
            operator.push(item)
            if
        elif item ==')':
            while '(' in operator:
                output.append(str(operator.top))
                operator.pop()


