#!/usr/bin/python
# -*- coding: Utf-8 -*-

osef = False
while not osef:
    nb = str(input("Binaire a convertir: "))
    for i in range(0,len(nb)):
        if nb[i] != "0" and nb[i] != "1":
            osef = False
            print("Ne pas utiliser de chiffre autre que 0 ou 1.")
            break
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
