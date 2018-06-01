def is_palindrome(input_str,low,high):
    if(low>=high):
        return True

    else:
        if input_str[0]==input_str[-1]:
            return is_palindrome(input_str[low+1:high-1],low+1,high-1)
        else:
            return False


def main():
    input_str="kayak"
    print(is_palindrome(input_str,0,5))

main()