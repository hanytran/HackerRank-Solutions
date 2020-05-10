#!/bin/python3
import os

def permutationEquation(p):
    out = []
    d = {}
    for i in sorted(p):
        d[i] = d.get(i, p.index(i)+1)
        out.append(p.index(d[i])+1)
    return out

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input())
    p = list(map(int, input().rstrip().split()))
    fptr.write('\n'.join(map(str, permutationEquation(p))))
    fptr.write('\n')
    fptr.close()