# #!/bin/python3
import os

def appendAndDelete(s, t, k):
    s_len = len(s)
    c = 0
    for i in range(1, min(len(t)+1, s_len+1)):
        if s[:i] == t[:i]:
            c = i
    len_not_match_s = s_len - c # string not match t -> should be removed
    operations = k - len_not_match_s # no. operations left
    len_need_change_s = len(t) - c
    if operations >= c*2 + len_need_change_s: # *2 used for empty and then put back
        return "Yes"
    if operations >= len_need_change_s and (operations - len_need_change_s) % 2 == 0:
        return "Yes"
    return "No"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    result = appendAndDelete(input(), input(), int(input()))
    fptr.write(result + '\n')
    fptr.close()