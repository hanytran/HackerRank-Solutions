#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
cnt = 0
b =[]
for i in range(n):
    for j in range(0, n-1):
        if a[j]>a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            cnt += 1
    if cnt==0: break
print('Array is sorted in {} swaps.'.format(cnt))
print('First Element: {}\nLast Element: {}'.format(a[0], a[-1]))