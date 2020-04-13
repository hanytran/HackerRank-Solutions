import re

sentences = '\n '.join(input().strip() for _ in range(int(input())))
for _ in range(int(input())):
    print(len(re.findall(r'\w%s\w' % input().strip(), sentences)))