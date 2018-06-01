def findChange(lst01):
    result=[count for count,elem in enumerate(lst01) if elem==1];
    return result[0]

def main():
    lst01=[0,0,0,0,0,1,1,1]
    print(findChange(lst01))

