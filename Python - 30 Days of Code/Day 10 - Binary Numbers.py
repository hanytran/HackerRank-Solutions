import re
if __name__ == '__main__':
    print(len(max(re.findall('[1]+', '{:b}'.format(int(input()))))))