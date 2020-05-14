#!/bin/python3
import os

def cutTheSticks(arr):
    out = []
    while len(arr)>=1:
        out.append(len(arr))
        min_a = min(arr)
        arr = [i-min_a for i in arr if (i-min_a)>0]
    return out


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    int(input())
    result = cutTheSticks(list(map(int, input().rstrip().split())))
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()