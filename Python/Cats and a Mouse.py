#!/bin/python3
import os

def catAndMouse(x, y, z):
    xz = abs(x-z)
    yz = abs(y-z)
    return 'Cat A' if xz<yz else 'Cat B' if xz>yz else 'Mouse C'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for q_itr in range(int(input())):
        x, y, z = list(map(int, input().split()))
        result = catAndMouse(x, y, z)
        fptr.write(result + '\n')
    fptr.close()