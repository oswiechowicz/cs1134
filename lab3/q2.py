def intersectlst(lsta, lstb):
    lstc=[]
    for i in lsta:
        if i in lstb:
            lstc.append(i)
    return lstc

def main():
    lsta=[1,6,14,15]
    lstb=[2,6,14,19]
    print(intersectlst(lsta,lstb))

#in sorted list, whatever is less you incement it
#similar to q1

main()