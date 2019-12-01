#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())
    out = {True: 'Weird', False: 'Not Weird'}
    print(out[(N%2) or ((not N%2) and N in range(6,21))])