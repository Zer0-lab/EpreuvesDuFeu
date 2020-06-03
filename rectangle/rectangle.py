#!/usr/bin/python3
import sys

list1 = list(open("c1.txt"))
list2 = list(open("c2.txt"))

newList1 = []
newList2 = []

def toSepare(list, newList):
    for i in list:
        newList += i.split()
    return newList


print(toSepare(list1, newList1), toSepare(list2, newList2))


lastList1 = []
lastList2 = []

def toIntList(list, newList):
    for i in range(len(list)):
            newList.append(list[i])
    return newList

print(toIntList(newList1, lastList1), "\n" ,toIntList(newList2, lastList2))

def match(list, oList, i , j):
    x = 0
    while  x < len(list):
        y = 0
        while  y < len(list[x]):
            if(list[x][y] != oList[i+x][j+y]):
                return False
                pass
            y += 1
            pass
        x += 1
        pass
        return True
    pass


def posRectangle(list, oList):
    start = 0
    i = 0
    while i < len(oList):
        j = 0
        while j < len(oList[i]):
            if oList[i][j] == list[0][0]:
                if match(list, oList, i, j):
                    print("find ! ", oList[i][j], "in position " , i, j)
                    return True
                pass
            j += 1
            pass
        i += 1
        pass
    return False

print(posRectangle(lastList1, lastList2))
