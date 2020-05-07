#!/bin/python3

import math
import os
from functools import reduce

def lcm(a, b):
    return abs(a*b)//math.gcd(a, b)

def getTotalX(a, b):
    lcm_a = reduce(lcm, a)
    gcd_b = reduce(math.gcd, b)
    tmp = []
    if gcd_b%lcm_a==0: tmp = [gcd_b]
    tmp += [i*lcm_a for i in range(1, gcd_b//lcm_a) if gcd_b%(i*lcm_a)==0]    
    return len(tmp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    input()
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    fptr.write(str(getTotalX(arr, brr)) + '\n')
    fptr.close()