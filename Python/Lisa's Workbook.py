#!/bin/python3
import os
from itertools import count, zip_longest

def workbook(n, k, a):
    page = count(1)
#     return sum([len([1 for probs in zip_longest(*[iter(range(1, num_chpt_probs+1))]*k) if next(page) in probs]) for num_chpt_probs in a])
    cnt = 0
    for num_chpt_probs in a:
        for probs in zip_longest(*[iter(range(1, num_chpt_probs+1))]*k):
            if next(page) in probs:
                cnt+=1
    return cnt                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().rstrip().split()))
    fptr.write(str(reworkbook(n, k, arr)sult) + '\n')
    fptr.close()