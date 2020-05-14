#!/bin/python3
import os

def howManyGames(p, d, m, s):
    cnt = 0
    while True:
        s -= p
        if s<0: break
        cnt += 1 
        p = max(p-d, m)
    return cnt  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    p, d, m, s = list(map(int, input().split()))
    fptr.write(str(howManyGames(p, d, m, s)) + '\n')
    fptr.close()