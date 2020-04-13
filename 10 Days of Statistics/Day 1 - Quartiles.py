n, arr = int(input()), sorted(list(map(int, input().split())))
from statistics import median
print(int(median(arr[:n//2])), int(median(arr)), int(median(arr[(n+1)//2:])), sep='\n')