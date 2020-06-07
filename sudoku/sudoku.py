#!/usr/bin/python3

sudoku = list((open("s.txt")))

sudoku2 = []
sudoku3 = []
listNbr = ["1","2","3","4","5","6","7","8","9"]
missNumber = "?"


def toSepare(list):
    newList = []
    for i in list:
        newList += i.split()
    return newList

sudoku = toSepare(sudoku)

def replaceToZero(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i] = list[i].replace("_", "0")
    return list

replaceToZero(sudoku)

print('\n'.join(sudoku))

def notInLine(k, list, i):
    for i in range(len(list)):
        if list[i][j] == k:
            return False;
    return True;


def notInRow(k, list, j):
    for j in range(len(list)):
        if list[i][j] == k:
            return False;
    return True;

def notInBlock(k, list, i, j):
    iBis = int((i / 4) * 4)
    jBis = int((j / 4) * 4)
    i = 0
    for i in range(iBis + 3):
        for j in range(jBis + 3):
            if list[iBis][jBis] == k:
                return False;
            j += 1
        i += 1
    return True;

for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
            if sudoku[i][j] == "0":
                for k in listNbr:
                    if notInLine(k, sudoku, i) and notInRow(k, sudoku, j) and notInBlock(k, sudoku, i, j):
                        print(k ,i , j)
                        sudoku[i] = sudoku[i].replace("0", k, 1)


print("\n")
print('\n'.join(sudoku))
