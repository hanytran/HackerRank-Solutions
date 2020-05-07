#!/bin/python3

import os
from itertools import combinations

def divisibleSumPairs(n, k, ar):
	return len([x for x in combinations(range(n), 2) if (ar[x[0]]+ar[x[1]])%k==0])
    # it = [i for i in combinations(ar, 2)]
    # return len([i for i in it if sum(i)%k==0])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, k = list(map(int, input().split()))
    ar = list(map(int, input().rstrip().split()))
    fptr.write(str(divisibleSumPairs(n, k, ar)) + '\n')
    fptr.close()