#!/bin/python3
import os

from collections import Counter
def sockMerchant(n, ar):
    return sum([i//2 for i in Counter(ar).values()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()