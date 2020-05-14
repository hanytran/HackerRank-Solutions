#!/bin/python3
import os
def minimumDistances(a):
    d = {}
    min_pair = len(a)
    for i, v in enumerate(a):
        if v in d:
            min_pair = min(i-d[v], min_pair)
        else: d[v] = i
    return min_pair if min_pair<len(a) else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    int(input())
    result = minimumDistances(list(map(int, input().rstrip().split())))
    fptr.write(str(result) + '\n')
    fptr.close()