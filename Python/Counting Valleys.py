#!/bin/python3
import os

def countingValleys(n, s):
    z_level = 0
    cnt = 0
    for i in s:
        if i=='U': 
            cnt+=1
            if cnt==0: z_level+=1
        else: cnt-=1       
    return z_level

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    fptr.write(str(countingValleys(n, s)) + '\n')
    fptr.close()