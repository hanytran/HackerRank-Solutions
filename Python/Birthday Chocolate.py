#!/bin/python3
import os

def birthday(s, d, m):
    cnt = 0
    if len(s)>1:
        for i in range(len(s)-m+1):            
            print(i, s[i:i+m])
            if (sum(s[i:i+m])==d): cnt+=1
    elif (m==1) and (sum(s)==d): return 1
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    d, m = list(map(int, input().rstrip().split()))
    fptr.write(str(birthday(s, d, m)) + '\n')
    fptr.close()