#!/usr/bin/python3
import sys

sentence = str(sys.argv[1::])
newSentence = " "

for i in range(len(sentence)):
    if i % 2 == 0:
        newSentence+= sentence[i].upper()
    else:
        newSentence+= sentence[i].lower()

print(str(newSentence))
