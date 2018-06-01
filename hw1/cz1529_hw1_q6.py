class Vector :
    def __init__(self, d) :
        #PART A
        self.coords=[]
        if isinstance(d, int):
            self.coords = [0]*d
        else:
            for i in d:
                self.coords.append(i)


    def __len__( self ) :
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__( self ,j,val ):
        self.coords[j] = val

    def __add__( self , other ):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__( self , other ) :
        return self.coords == other.coords

    def __ne__( self , other ) :
        return not (self == other)

    def __str__( self ) :
        return '<'+ str(self.coords)[1:-1] + '>'

    def __repr__( self ) :
        return str(self)

    #PART B
    def __sub__(self, other):
        if (len(self) != len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    #PART C
    def __neg__(self):
        for i in range(len(self.coords)):
            self.coords[i]=(-self.coords[i]);
        return self

    #PART D
    def __mul__(self, other):
        #PART F
        #determines if vector or scalar then performs task
        if isinstance(other, int):
            for i in range(len(self.coords)):
                self.coords[i]=(self.coords[i]*other)
            return self

        else:
            if (len(self) != len(other)):
                raise ValueError("dimensions must agree")
            for i in range(len(self.coords)):
                self.coords[i]=(self.coords[i]*other.coords[i])
            final=sum(self.coords)
            return final


    #PART E
    def __rmul__(self, other):
        for i in range(len(self.coords)):
            self.coords[i]=(self.coords[i]*other)
        return self

def main():
    vector2=Vector([4,7,5])
    vector3=Vector([2,6,4])

    print(vector2*vector3)
