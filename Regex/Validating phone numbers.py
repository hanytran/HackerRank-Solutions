import re
print(*['YES' if (bool(re.match(r'^[789]\d{9}$', input()))) else 'NO' for _ in range(int(input()))], sep='\n')