#!/usr/bin/python3
import sys

number = 9
rangeNumber = range(number)

def factorial(nb):
    nbRange = range(nb)
    for i in nbRange[::-1]:
        if i >= 1:
            nb = nb*i
            print(nb, i)
        else:
            return nb


print("Le factorielle de %s est %s " % (number, factorial(number)))