#!/bin/python3
import os

def angryProfessor(k, a):
    print(k, a)
    return 'NO' if len([i for i in a if i<=0])>=k else 'YES'

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for t_itr in range(int(input())):
        _, k = list(map(int, input().split()))
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
        fptr.write(result + '\n')
    fptr.close()