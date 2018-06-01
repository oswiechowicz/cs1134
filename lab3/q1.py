def reverse_vowels(input_str):
    lst=[]
    for i in range(len(input_str)):
        if (input_str[i]=="a" or input_str[i]=="e" or input_str[i]=="i" or input_str[i]=="o" or input_str[i]=="u") and (len(lst)==0):
            lst.append(i)
        elif (input_str[i]=="a" or input_str[i]=="e" or input_str[i]=="i" or input_str[i]=="o" or input_str[i]=="u") and (len(lst)==1):
            input_str[i],input_str[lst[0]]=input_str[lst[0]],input_str[i]
            return input_str

    return None

def main():
    str="tandon"
    print(reverse_vowels(str))

main()