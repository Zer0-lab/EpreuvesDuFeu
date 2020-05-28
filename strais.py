#!/usr/bin/python3
import sys

nb_marche = int(sys.argv[1])

def stairs(nbMarche):
    for i in range(nbMarche):
        print((nbMarche-i-1) * " " + "$" * (i+1))

    for i in range(nbMarche):
        print((nbMarche-i) * " " + i * "$ ")

    for i in range(nbMarche):
        print((nbMarche-i) * +i * "$")

stairs(nb_marche)
