import numpy as np
from scipy import stats

n, arr = int(input()), list(map(int, input().split()))
print('{:.1f}'.format(np.mean(arr)))
print('{:.1f}'.format(np.median(arr)))
print(int(stats.mode(arr)[0]))