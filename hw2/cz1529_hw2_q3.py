import math

def factors(n):
    lst=[]
    for i in range(1,int(math.sqrt(n))):
        if n%i==0:
            if n//i != 0: #n/i will equal a factor but must make sure it is not equal to i
                yield i #yield generator if factor
                yield n//i

#I'm a bit confused on how to get them to print in order while
#keeping sqrt(n) run time

def main():
    for curr_factor in factors(100):
        print(curr_factor)

main()