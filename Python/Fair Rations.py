def fairRations(B):
    if sum(B)%2: return 'NO'
    cnt = 0
    for i in range(len(B)):
        if B[i]%2: 
            cnt += 2
            B[i+1] += 1
    return str(cnt)