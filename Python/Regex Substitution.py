import re
# print(re.sub(r' \|\| ', ' or ', re.sub(r' &&(?= )',' and', '\n'.join([input() for _ in range(int(input()))]))))
print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group()=='&&' else 'or', '\n'.join([input() for _ in range(int(input()))])))