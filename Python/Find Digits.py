#!/bin/python3
import os
import itertools

def findDigits(n):
    a = [int(j) for j in str(n) if int(j)>0]
    return len([i for i in a if n%i==0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for t_itr in range(int(input())):
        fptr.write(str(findDigits(int(input()))) + '\n')
    fptr.close()