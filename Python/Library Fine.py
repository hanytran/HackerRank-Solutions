#!/bin/python3
import os

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2: return 10000
    if (y1==y2): 
        if (m1>m2): return 500*(m1-m2)
        if (m1==m2) and (d1>d2): return 15*(d1-d2)
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    d1, m1, y1 = list(map(int, input().split()))    
    d2, m2, y2 = list(map(int, input().split()))
    fptr.write(str(libraryFine(d1, m1, y1, d2, m2, y2)) + '\n')
    fptr.close()