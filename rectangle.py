#!/usr/bin/python3
import sys

list1 = list(open("c1.txt"))
list2 = list(open("c2.txt"))

newList1 = [""]
newList2 = [""]
finalList1 = []
finalList2 = []

def removeSpace(list):
    i = 0
    while i != len(list):
        list[i] = list[i].replace("\n", "")
        i += 1
    return list

print(removeSpace(list1), "\n", removeSpace(list2))

def concatList(list, newList):
    for i in list:
        newList[0] = newList[0] +  i
    return newList

print(concatList(list1, newList1), "\n", concatList(list2, newList2))



def toSepare(list, newList):
    i = 0
    while i < len(list[0]):
        newList += list[0][i].split(" ")
        i += 1
    return newList

print(toSepare(newList1, finalList1), "\n", toSepare(newList2, finalList2))


def toIntList(list, newList):
    for i in list:
        newList.append(int(i))
    return newList

lastList1 = []
lastList2 = []

print(toIntList(finalList1, lastList1), "\n",toIntList(finalList2, lastList2))


start, end = 0, 0
isTheEnd = False
count = 0
print(start, end)
print(count, isTheEnd)
for i in lastList2:
    for j in lastList1:
        if i == j and start == 0:
            start =  lastList2.index(i)+ 1
            # print("le debut du rectangle commence ici", start)
        elif isTheEnd == True and end == 0 :
            end = lastList2.index(i)
            print(end)
        elif count == len(lastList1):
            isTheEnd = True
        elif i == j:
            count += 1
            print("count ",count)

print(start, end)
print(count, isTheEnd)
