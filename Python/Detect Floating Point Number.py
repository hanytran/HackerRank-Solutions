import re
print('\n'.join([str(bool(re.match(r'^[+-]?[0-9]*\.[0-9]+$', input()))) for _ in range(int(input()))]))