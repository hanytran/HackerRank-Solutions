import re
S, k = input(), input()
pattern = re.compile(k)
r = pattern.search(S)
if not r: print("(-1, -1)")
else: 
    while r:
        print("({}, {})".format(r.start(), r.end()-1))
        r = pattern.search(S, r.start()+1)