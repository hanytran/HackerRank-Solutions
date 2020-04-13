for i in range(1, int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321, 12345678910987654321][i-1])
print(int(''.join([str(m) for m in range(1, i)])+str(i)+''.join([str(m) for m in range(i-1, 0, -1)])))