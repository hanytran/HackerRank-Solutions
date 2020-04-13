import math
a = [int(input()) for _ in range(int(input()))]
for i in a:
    prime = ['Prime', 'Not prime']
    tmp = 0
    if i>3:    
        for j in range (2, int(math.sqrt(i))+1):
            if i%j==0: 
                tmp = 1
                break
    if i==1: print(prime[1])
    else: print(prime[tmp])