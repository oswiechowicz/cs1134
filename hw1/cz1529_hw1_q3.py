#Part A
def squaresums(n):
    lst=[i**2 for i in range(n)]
    sum=0
    for i in lst:
        sum+=i;
    return sum

#Part B
def squaresumsb(n):
    return sum([i**2 for i in range(n)])

#Part C
def oddsquaresum(n):
    lst=[]
    for i in range(n):
        if not i%2==0:
            lst.append(i);
    lst=sum(lst)
    return lst

#Part D
def oddsumsquareb(n):
    return sum(i for i in range(n) if not i%2==0)

def main():
    print(squaresums(7));
    print(squaresumsb(7));
    print(oddsquaresum(7))
    print(oddsumsquareb(7))
