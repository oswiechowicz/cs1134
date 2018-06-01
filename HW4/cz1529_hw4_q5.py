#PART A
def count_lowercase(s, low, high):
    if low>high:
        return 0
    elif s[low].islower():
        return 1+count_lowercase(s,low+1,high)
    else:
        return 0+count_lowercase(s,low+1,high)

#PART B
def is_number_of_lowercase_even(s,low,high):
    total=0
    if low>high:
        return 0
    elif s[low].islower():
        total=1+count_lowercase(s,low+1,high)
    else:
        total=0+count_lowercase(s,low+1,high)
    if total%2==0:
        return True
    else:
        return False




def main():
    s='CoNNiEh'
    print(count_lowercase(s,0,6))
    print(is_number_of_lowercase_even(s,0,6))
