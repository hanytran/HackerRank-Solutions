#!/bin/python3
import os

def circularArrayRotation(a, k, queries):
    b = a[(len(a)-k):] + a[:(len(a)-k)]
    return [b[i] for i in queries]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n, k, q = list(map(int, input().split()))
    a = list(map(int, input().rstrip().split()))
    queries = [int(input()) for _ in range(q)]        
    result = circularArrayRotation(a, k, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
    

n, k, q = map(int, input().split())
a = list(map(int, input().rstrip().split()))
print(*[a[int(input()) - k % len(a)] for _ in range(q)], sep="\n")