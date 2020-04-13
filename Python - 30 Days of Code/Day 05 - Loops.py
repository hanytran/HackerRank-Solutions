if __name__ == '__main__':
    n = int(input())
    print('\n'.join(['{} x {} = {}'.format(n, i, n*i) for i in range(1, 11)]))