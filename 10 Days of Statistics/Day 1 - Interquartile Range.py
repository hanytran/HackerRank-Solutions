_, arr, fr = input(), map(int, input().split()), map(int, input().split())
mylist = []
for i, j in zip(arr, fr):
    mylist += [i]*j
mylist, n = sorted(mylist), len(mylist)
from statistics import median
print(round(float(median(mylist[(n+1)//2:]))-float(median(mylist[:n//2])), 1))