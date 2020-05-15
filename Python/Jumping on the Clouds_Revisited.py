#!/bin/python3
import os

def jumpingOnClouds(c, k, n):
    next = k%n
    e = 100
    while True:
        e = e - c[next]*2 - 1
        if next==0: return e
        next = (next+k)%n      


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, k = list(map(int, input().split()))
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k, n)
    fptr.write(str(result) + '\n')
    fptr.close()
