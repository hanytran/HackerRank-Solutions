#!/bin/python3
import os

def viralAdvertising(n):
    num = 5
    likes = 2
    for _ in range(2, n+1):
        num = (num//2)*3
        likes += num//2
    return likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(str(viralAdvertising(int(input()))) + '\n')
    fptr.close()