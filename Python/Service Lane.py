#!/bin/python3
import os

# Complete the serviceLane function below.
def serviceLane(width, cases):
    return [min(width[v[0]:v[1]+1]) for v in cases]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _, t = input().split()
    width = list(map(int, input().rstrip().split()))
    cases = [list(map(int, input().rstrip().split())) for _ in range(t)]
    fptr.write('\n'.join(map(str, serviceLane(width, cases))))
    fptr.write('\n')
    fptr.close()