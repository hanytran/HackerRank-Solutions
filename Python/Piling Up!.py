for _ in range(int(input())):
    l = int(input())
    lst = list(map(int, input().split()))
    i = 0
    while (i < l - 1) and (lst[i] >= lst[i+1]):
        i += 1
    while (i < l - 1) and (lst[i] <= lst[i+1]):
        i += 1
    print("Yes") if i == l - 1 else print("No")
# for _ in range(int(input())):