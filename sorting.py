#!/usr/bin/python3
import sys

listUnsorted = [1, 34, 546, 43, 2, 4689, 422]#sys.argv[1::]
sortedList = []

for i in listUnsorted:
    sortedList.append(i)



def descending(list):
    descendingList = []
    for i in list:
        descendingList.append(int(i))
        descendingList  = sortedList[::-1]
    return descendingList

def bubble(list):
    bubbleList = list.copy()
    lenList = len(bubbleList)
    for i in range(lenList):
        for j in range(0, lenList-i-1):
            if bubbleList[j] > bubbleList[j+1]:
                bubbleList[j], bubbleList[j+1] = bubbleList[j+1], bubbleList[j]
    return bubbleList

def select(list):
    selectList = list.copy()
    lenList = len(selectList)
    for i in range(1, lenList-1):
        min = i
        for j in range(i+1, lenList):
            if selectList[j] < selectList[min]:
                min = j
        if min != i:
            selectList[i], selectList[min] = selectList[min], selectList[i]
    return selectList




print("Voici la liste trié décroissante : %s" % descending(sortedList))
print("Voici la liste trié avec un tri bulle : %s" % bubble(sortedList))
print("Voici la liste trié avec un tri par selection : %s" % select(sortedList))


"""
[10, 9, 5, 7, 3]    # Tableau à trier
[3,| 9, 5, 7, 10]   # 3 est le plus petit élément. On l'échange avec 10. Sous-tableau gauche trié : [3]
[3, 5,| 9, 7, 10]   # On échange 5 avec 9. Sous-tableau gauche trié : [3,5]
[3, 5, 7,| 9, 10]   # On échange 7 avec 9. Sous-tableau gauche trié : [3,5,7]
[3, 5, 7, 9,| 10]   # Sous-tableau gauche trié : [3,5,7,9]
[3, 5, 7, 9, 10]    # Sous-tableau gauche trié : [3,5,7,9,10]. Fin.
"""
