from itertools import groupby
print(*[(len([*j]), int(k)) for k, j in groupby(input())])