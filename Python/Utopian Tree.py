#!/bin/python3
import os

def utopianTree(n):
    return ~(~1<<(n>>1)) << n%2
    # h = 1
    # if n==0: return h
    # for i in range(1, n+1):        
    #     if i%2!=0: h=h*2
    #     else: h += 1
    # return h

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    for t_itr in range(int(input())):
        fptr.write(str(utopianTree(int(input()))) + '\n')
    fptr.close()