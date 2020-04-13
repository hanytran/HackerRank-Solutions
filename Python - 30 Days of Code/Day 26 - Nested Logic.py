n, m = [map(int, input().split()) for _ in range(2)]
d, m, y = [i-j for i,j in zip(n,m)]
if y>0: print(10000)
elif y==0:
    if m>0: print(500*m)
    elif d>0: print(d*15)
    else: print(0)
else: print(0)