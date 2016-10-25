#!/usr/bin/python
# -*- coding: Utf-8 -*-

osef = False
while not osef:
    nb = str(input("Binary to convert: "))
    if nb.count("1") + nb.count("0") != len(nb):
        print("Don't use other numbre that 0 or 1.")
    else:
        osef = True

a = 0
b = 1
i = len(nb) - 1
while i != -1:
    if nb[i] == "1":
        a += b
    b = b * 2
    i-=1

print(int(a))
