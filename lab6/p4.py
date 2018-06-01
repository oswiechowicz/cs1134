import ctypes

def make_array(n):
    return(n*ctypes.py_object)()

class MyString:
    def __init__(self,initial_str=""):
        self.string=initial_str
        self.n=len(initial_str)

    def __len__(self):
        n=0
        for char in self.string:
            n+=1
        return n

    def __iter__(self):
        for i in range(len(self.string)):
            yield i

    def __repr__(self):
        return self.string

   # def get_item(self,k):
   #     if not 0<(len(self.string)-1)<k:
   #         raise IndexError("invalid index")
   #     else:
   #         return self.string[k]


    def __add__(self, other):
        return MyString('connie'+'zhou')

def main():
    s=MyString("connie")
    s2=MyString("zhou")
    print(s)
    print(len(s))
    print(s+s2)

main()