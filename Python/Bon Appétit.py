#!/bin/python3
def bonAppetit(bill, k, b):
    print('Bon Appetit' if (sum(bill)-bill[k])/2==b else int(b-(sum(bill)-bill[k])/2))

if __name__ == '__main__':
    n, k = list(map(int, input().rstrip().split()))
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)