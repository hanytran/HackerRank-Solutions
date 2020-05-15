#!/bin/python3
import os

def jumpingOnClouds(c):
    cnt = 0
    i = 0
    while i<len(c)-1:
        if (i<len(c)-2) and not c[i+2]:
            i+=1       
        i+=1
        cnt+=1
       
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input())
    result = jumpingOnClouds(list(map(int, input().rstrip().split())))
    fptr.write(str(result) + '\n')
    fptr.close()