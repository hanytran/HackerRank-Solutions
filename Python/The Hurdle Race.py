#!/bin/python3
import os

def hurdleRace(k, height):
    return max((max(height)-k), 0)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, k = list(map(int, input().split()))
    height = list(map(int, input().rstrip().split()))
    fptr.write(str(hurdleRace(k, height)) + '\n')
    fptr.close()