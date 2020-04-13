# d = {}
# for _ in range(int(input())):
#     n = input()
#     d[n] = d.get(n, 0) + 1
# print(len(d))
# print(*d.values())
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())