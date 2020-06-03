#!/usr/bin/python3
import sys

wordList = list(open("fr.txt"))
anagram = str(sys.argv[1::])
#anagram = "arbre"


def removeSpace(list):
    newList =[]
    for i in list:
        newList.append(i.strip())
    return newList

def toSepare(word):
    word2 = ""
    for i in sorted(word):
        word2 += ''.join(i)
    return word2

wordList = removeSpace(wordList)

i = 0
while i < len(wordList):
    if toSepare(wordList[i]) == toSepare(anagram):
        if(wordList[i] != anagram):
            print("L'anagrame de %s est %s " % (anagram, wordList[i]))
    i += 1
