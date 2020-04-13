#!/bin/python3

# from datetime import datetime as dt
# fmt = '%a %d %b %Y %H:%M:%S %z'
# for i in range(int(input())):
#     print(int(abs((dt.strptime(input(), fmt) - 
#                    dt.strptime(input(), fmt)).total_seconds())))
from dateutil import parser
for _ in range(int(input())):
    print(abs(int((parser.parse(input().strip())-parser.parse(input().strip())).total_seconds())))
