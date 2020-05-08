#!/bin/python3
import os

def beautifulDays(i, j, k):
    return len([m for m in range(i, j+1) if (abs(int(str(m)[::-1]))-m)%k==0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    i, j, k = list(map(int, input().split()))
    fptr.write(str(beautifulDays(i, j, k)) + '\n')
    fptr.close()