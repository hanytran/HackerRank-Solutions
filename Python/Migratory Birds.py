#!/bin/python3
import os

def migratoryBirds(arr):
    count = [0]*6
    for t in arr:
        count[t] += 1
    return count.index(max(count))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input().strip())
    result = migratoryBirds(list(map(int, input().rstrip().split())))
    fptr.write(str(result) + '\n')
    fptr.close()