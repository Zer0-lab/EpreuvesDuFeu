#!/usr/bin/python3
import sys

list = sys.argv[1::]
descList = []

for i in list:
    descList.append(int(i))

descList.sort()

print(descList[::-1])
