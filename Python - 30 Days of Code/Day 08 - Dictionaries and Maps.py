n = int(input())
mydict = {}
for _ in range(n):
    i, j = input().split()
    mydict[i] = j
for _ in range(n):
    n = input()
    print('{}={}'.format(n, mydict[n]) if n in mydict.keys() else 'Not found')