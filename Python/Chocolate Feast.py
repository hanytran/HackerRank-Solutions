#!/bin/python3
import os

# Complete the chocolateFeast function below.
def chocolateFeast(n, c, m):
    wrappers = n//c
    cnt = wrappers
    while (wrappers)>=m:
        cnt += wrappers//m 
        wrappers = wrappers//m + wrappers%m

    return cnt 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for t_itr in range(int(input())):
        n, c, m = list(map(int, input().split()))
        fptr.write(str(chocolateFeast(n, c, m)) + '\n')
    fptr.close()