#!/bin/python3
import os

def repeatedString(s, n):
    return n//len(s)*s.count('a') + s[:(n%len(s))].count('a')


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    fptr.write(str(repeatedString(s, n)) + '\n')
    fptr.close()