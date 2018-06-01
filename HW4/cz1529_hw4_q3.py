#PART A

def print_triangle(n):
    if n<=0:
        return
    else:
        print_triangle(n-1)
        print(n*'*')

#PART B
def print_opposite_triangle(n):
    if n<=0:
        return
    else:
        print(n*'*')
        print_opposite_triangle(n-1)
        print(n*'*')

#PART C
def print_ruler(n):
    if(n == 0):
        return
    print_ruler(n-1)
    print("-"*n)
    print_ruler(n-1)


def main():
    print_ruler(4)



