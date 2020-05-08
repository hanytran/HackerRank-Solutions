#!/bin/python3

import os
from itertools import product

def getMoneySpent(keyboards, drives, b):
    c = [sum(m) for m in product(keyboards, drives) if sum(m)<=b]
    return max(c) if c else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    b, n, m = list(map(int, input().split()))
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))
    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()