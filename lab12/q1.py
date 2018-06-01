import csv
from binarysearchtree import *

def height_sizes(n):
    bst=BinarySearchTreeMap()
    bst.insert()

def create_csv(sizes_lst,heights_lst):
    file=open('heights.csv','w')
    if len(sizes_lst) != len(heights_lst):
        raise Exception("list given must be of equal sizes")
    for i in range(len(sizes_lst)):
        file.write(str(sizes_lst[i])+","+str(heights_lst[i])+'\n')
    file.close()

