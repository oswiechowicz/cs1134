import random
#PARTA
#runtime=(theta(n^2))

#part b
def roll_the_dice_str(n):
    ' '.join([random.randint(1,6) for i in range(n)])

#QUESTION 3
def move_zeroes(nums):
    length=len(nums)
    lst=[lst.pop[i] for i in range(len(nums))]
