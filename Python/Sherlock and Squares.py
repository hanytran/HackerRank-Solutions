#!/bin/python3

import math
import os

def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = int(math.sqrt(b))
    return len(range(x, y+1))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for q_itr in range(int(input())):
        a, b = list(map(int, input().split()))
        fptr.write(str(squares(a, b)) + '\n')
    fptr.close()