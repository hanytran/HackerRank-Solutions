#!/bin/python3
import os

def designerPdfViewer(h, word):
    return max((h[ord(c)-97] for c in word)) * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = list(map(int, input().rstrip().split()))
    fptr.write(str(designerPdfViewer(h, input())) + '\n')
    fptr.close()