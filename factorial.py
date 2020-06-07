#!/usr/bin/python3
import sys

number = 42

#int(sys.argv[1])

def factorial(nb):
    nbRange = range(nb)
    for i in nbRange[::-1]:
        if i >= 1:
            nb = nb*i
            return nb


print("Le factorielle de %s est %s " % (number, factorial(number)))
