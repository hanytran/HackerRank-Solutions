import re
r = r'(?<!^)(#(?:[\da-f]{3}){1,2})'
for _ in range(int(input())):
    t = re.findall(r, input(), flags=re.I)
    if t:
        print(*t, sep='\n')