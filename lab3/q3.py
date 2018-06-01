def square_root(num):
    result=1
    i=0.01
    while result<=num:
        result=i*i
        if result==num:
            return i
        i+=0.01


#0.01*0.01
#0.02 * 0.02
#run time theta(100sqrt(n))=sqrt(n)

#LOG N PART (newtonion method and babylonian method)
