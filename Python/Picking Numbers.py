#!/bin/python3
import os
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.

def pickingNumbers(a):
    return max(len([x for x in a if 0 <= u - x <= 1]) for u in set(a))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    fptr.write(str(result) + '\n')
    fptr.close()