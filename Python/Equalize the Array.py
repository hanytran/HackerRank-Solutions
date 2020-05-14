#!/bin/python3
import os
from collections import Counter

def equalizeArray(arr):
    return len(arr)-max(Counter(arr).values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    int(input())
    result = equalizeArray(list(map(int, input().rstrip().split())))
    fptr.write(str(result) + '\n')
    fptr.close()