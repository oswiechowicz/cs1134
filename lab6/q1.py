def powers_of_two(num):
    for i in range(1,num+1):
        yield 2**i

def main():
    for curr_value in powers_of_two(6):
        print(curr_value)

main()
