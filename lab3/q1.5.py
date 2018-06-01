def reverse_vowels(input_str):
    lst=list(input_str) #turns it into a mutable list
    i=0 #start of str
    j=len(input_str)-1 #end of str

    while i<j:
        if not (lst[i]=="a" or lst[i]=="e" or lst[i]=="i" or lst[i]=="o" or lst[i]=="u"):
            i+=1 #keeps going up til finds a vowel

        elif not(lst[j] == "a" or lst[j] == "e" or lst[j] == "i" or lst[j] == "o" or lst[j] == "u"):
            j-=1 #when i finds a vowel, iterate j til its a vowel

        else: #when theyre both vowels
            lst[i],lst[j]=lst[j],lst[i]
            i+=1
            j-=1
    return "".join(lst)

def main():
    str="tandon"
    print(reverse_vowels(str))

main()
