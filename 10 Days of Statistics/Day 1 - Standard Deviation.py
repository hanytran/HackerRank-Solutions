n, arr = int(input()), list(map(int, input().split()))
mean = sum(arr)/n
import math
print(round(math.sqrt(sum([(i-mean)**2 for i in arr])/n), 1))