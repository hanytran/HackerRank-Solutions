import email.utils
import re
for _ in range(int(input())):
    t = email.utils.parseaddr(input())
    if bool(re.match(r'^[a-zA-Z](\w|-|_|\.)+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', t[1])):
        print(email.utils.formataddr(t))