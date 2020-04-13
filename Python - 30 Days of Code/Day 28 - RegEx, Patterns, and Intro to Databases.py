#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    a = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]        
        emailID = firstNameEmailID[1]
        if (firstName+'@gmail.com' in emailID): a.append(firstName)

    print(*sorted(a), sep='\n')