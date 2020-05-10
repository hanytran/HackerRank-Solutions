#!/bin/python3
import os

def saveThePrisoner(n, m, s):
    return n if (m+s-1)%n==0 else (m+s-1)%n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for t_itr in range(int(input())):
        n, m, s = list(map(int, input().split()))        
        fptr.write(str(saveThePrisoner(n, m, s)) + '\n')
    fptr.close()