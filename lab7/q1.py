import ArrayStack

def is_matched(expr):
    lefty='({['
    righty=')}]'

    S=ArrayStack()

    for token in expr:
        if token in lefty:
            S.push(token)
        elif token in righty:
            if S.is_empty():
                return False
            from_S=S.top()
            if (righty.index(token)==lefty.index(from_S)):
                S.pop()
            else:
                return False
        else:
            raise ValueError
    return S.is_empty()


def get_tag(text):
    start=0
    end=0
    for i in text():
        if text[i]=='<':
            start=i
        elif text[i]=='>':
            end=i
    yield '<'+text[start:end]+'>'



def is_matched_html(expr):
    S=ArrayStack()
    expr.find('<')
    while j!=-1:
        k=expr.find('>',j+1)
        if k==-1:
            return False
        tag=expr[j+1:k]
        if not tag.startswith('/'):
            S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:]!=S.pop():
                return False
        j=expr.find('<',k+1)
    return S.is_empty()
