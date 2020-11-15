
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

data = pd.read_csv(open('C:\Users\remit\OneDrive\Bureau\EIVP\Programmation\ProjetPython'),sep=';')
print (data)

noise=data["noise"].tolist()
print(noise)
temp=data["temp"].tolist()
hum=data["humidity"].tolist()
lum=data["lum"].tolist()
co2=data["co2"].tolist()
date=data["sent_at"].tolist()

def maximum(Colonne_Noise):
    max=Colonne_Noise[0]
    n=len(Colonne_Noise)
    for i in range(n):
        if Colonne_Noise[i]>=max:
            max=Colonne_Noise[i]
    return max

def minimum(Colonne_Noise):
    min=Colonne_Noise[0]
    n=len(Colonne_Noise)
    for i in range(n):
        if Colonne_Noise[i]<=min:
            min=Colonne_Noise[i]
    return min

def somme(Colonne_Noise):
    som = 0
    for k in Colonne_Noise:
        som = som + k
    return som

def moyenne(Colonne_Noise):
    return somme(Colonne_Noise)/len(Colonne_Noise)

def insertionSort(Colonne_Noise):
    for i in range(1, len(Colonne_Noise)):
        key = Colonne_Noise[i]
        j = i-1
        while j >= 0 and key < Colonne_Noise[j]:
            Colonne_Noise[j + 1] = Colonne_Noise[j]
            j-= 1
            Colonne_Noise[j + 1] = key
    return Colonne_Noise

def mediane(Colonne_Noise):
    n = len(Colonne_Noise)
    if n< 1:
        return None
    if n % 2 == 0 :
        return ( Colonne_Noise[(n-1)/2] + Colonne_Noise[(n+1)/2] ) / 2.0
    else:
        return Colonne_Noise[(n-1)/2]
