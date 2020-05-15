#!/bin/python3
import os

def beautifulTriplets(d, arr, n):
    cnt = 0
    for i in range(n):
        if (arr[i]+d in arr) and (arr[i]+2*d in arr):
            cnt+=1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, d = list(map(int, input().split()))
    arr = list(map(int, input().rstrip().split()))
    fptr.write(str(beautifulTriplets(d, arr, n)) + '\n')
    fptr.close()