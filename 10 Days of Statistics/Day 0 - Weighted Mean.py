_, arr, w = int(input()), list(map(int, input().split())), list(map(int, input().split()))
sumw = sum(w)
mysum = sum([i*j for i, j in zip(arr,w)])
print(round(mysum/sumw, 1))