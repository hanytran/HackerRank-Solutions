#!/bin/python3

import os
# Complete the breakingRecords function below.
def breakingRecords(scores):
    low, high = scores[0], scores[0]
    l_cnt, h_cnt = 0, 0
    for i in scores:
        if i<low: 
            low = i
            l_cnt+=1
        if i>high: 
            high = i
            h_cnt+=1
    return h_cnt, l_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    _ = int(input())
    scores = list(map(int, input().rstrip().split()))
    fptr.write(' '.join(map(str, breakingRecords(scores))))
    fptr.write('\n')
    fptr.close()