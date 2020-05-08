#!/bin/python3
import os

def pageCount(n, p):
    return min(p//2, n//2-p//2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    fptr.write(str(pageCount(n, p)) + '\n')
    fptr.close()