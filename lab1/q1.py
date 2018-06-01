class Polynomial:
    def __init__(self,list=[]):
        self.coeffs=list;

    #def __repr__(self):
    #    self.s="p(x)="
    #    for i in range(len(self.coeffs),-1,-1):
    #        self.s = self, ((self.coeffs[i]), "x^", ((len(self.coeffs) - i)))
    #    return self.s

    def eval(self):
        return self

    def __add__(self, other):
        total=[]
        temp=0
        copy1=self.coeffs.copy()
        copy2=other.coeffs.copy()

        while len(copy1)<len(copy2):
            copy1.append(0);

        while len(self.coeffs)>len(other.coeffs):
            copy2.append(0);

        for i in range(len(copy1)):
            temp=copy1[i]+copy2[i]
            total.append(temp)

        return total

    def __mul__(self, other):
        copy1=self.coeffs
        copy2=other.coeffs
        polyToAdd=0
        total=[]
        place=0
        length = (len(self.coeffs) - 1) + (len(other.coeffs) - 1)
        while length > -1:
            total.append(0)
            length -= 1
        for i in range(len(copy1)):
            for j in range(len(copy2)):
                polyToAdd=copy1[i]*copy2[i]
                place=i+j
            total[place]=polyToAdd


        return total

def main():

    lst=[3,7,0,-9,2]
    lst2=[3,16,1,-9,2,0,0,0,0,9]
    lst3=[0,1,5]
    lst4=[0,1,3,0,0,0,0,0,2]
    p=Polynomial(lst3)
    print(p)
    p2=Polynomial(lst4)
    print(p+p2)
    print(p*p2)

main()