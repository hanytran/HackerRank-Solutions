#!/bin/python3
import re

n, m = map(int, input().rstrip().split())
matrix = [input() for _ in range(n)]
s = ''
for z in zip(*matrix):
    s += ''.join(z)
print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', s))