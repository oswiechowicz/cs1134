def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]]
    out = []
    for i in range(low, high+1):
        lst[i], lst[low] = lst[low], lst[i]
        for j in permutations(lst, low+1, high):
            rest = [lst[low]] + j
            out.append(rest)
        lst[i], lst[low] = lst[low], lst[i]
    return out

def main():
    lst=[1,2,3]
    print(permutations(lst,0,2))

