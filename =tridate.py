# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:11:20 2020

@author: remit
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from math import *
import csv
import statistics as st
import datetime 

data = pd.read_csv(r"C:\Users\remit/ProjetAlgo/EIVP_KM.csv",sep=';')

noise=data["noise"].tolist()
temperature=data["temp"].tolist()
humidite=data["humidity"].tolist()
luminosite=data["lum"].tolist()
co2=data["co2"].tolist()
date=data["sent_at"].tolist()
idcapteur=data["id"].tolist()



   
def Tri_date(date):
    n = len(date)
    for i in range(n-1):
        for j in range(0, n-i-1):    
            if date[j] > date[j+1] : 
                date[j], date[j+1] = date[j+1], date[j] 
                noise[j], noise[j+1] = noise[j+1], noise[j] 
                temperature[j], temperature[j+1] = temperature[j+1], temperature[j] 
                humidite[j], humidite[j+1] = humidite[j+1], humidite[j]
                luminosite[j], luminosite[j+1] = luminosite[j+1], luminosite[j] 
                co2[j], co2[j+1] = co2[j+1], co2[j]
    return date

def moyenne(Y):
    mo=0
    n=len(Y)
    for k in Y:
        mo += k
    mo=mo/n
    moy=round(mo,2)
    return moy
print("la moyenne est",moyenne(temperature))
def anomalies(data):
    if data==noise:
        larg=101
        pres=0.8
    if data==temperature:
        larg=202
        pres=0.8
    if data==luminosite:
        larg=2
        pres=0.95
    if data==humidite:
        larg=101
        pres=0.8
    if data==co2:
        larg=101
        pres=0.8
    print(larg, pres)
    Ano=[]
    DateAno=[]
    M=[]
    for i in range (len(data)):
        LG=[]
        LD=[]
        for k in range (1, larg):  #largeur
            if (i-k>-1):
                LG.append(data[i-k])  
            if (i+k<len(data)):
                LD.append(data[i+k])
        S=0
        C=LG+LD
        for j in range (len(C)):
            S=S+C[j]
        Moy=S/len(C)
        if (data[i]<Moy*(1-pres)) or (data[i]>(1+pres)*Moy):   #precision
            Ano.append(data[i])
            DateAno.append(date[i])
            M.append(Moy)
    return Ano,DateAno

print(anomalies(temperature))


def occup_bureau(noise):
    occ_bureau=[]
    for i in range(len(noise)):
        if noise[i]>33 and luminosite[i]>20:
            occ_bureau.append(date[i])
    return occ_bureau

ocbu=occup_bureau(noise)
print(len(ocbu))

def nonoccup_bureau(noise):
    nonocc_bureau=[]
    for i in range(len(noise)):
        if noise[i]<=33 and luminosite[i]<=20:
            nonocc_bureau.append(date[i])
    return nonocc_bureau

nocbu=nonoccup_bureau(noise)


def chiffrage(ocbu):
    c=[]
    for i in range(len(ocbu)):
        c.append(str(ocbu[i]))
    return c

c=chiffrage(ocbu)
print(len(c[1]))

def chiff(c):
    chif=[]
    for i in range(len(c)):
        for j in range(len(c[i])):
            chif.append(c[i][11:13]+c[i][14:16]+c[i][17:19])
    
    return  chif
ch=chiff(c)
print(ch)
print(max(ch))
print(min(ch))

debhor=min(ch)
finhor=max(ch)
debhora=str(debhor)
finhora=str(finhor)
debuthoraire=debhora[0:2]+":"+debhora[2:4]+":"+debhora[4:6]
finhoraire=finhora[0:2]+":"+finhora[2:4]+":"+finhora[4:6]
print("la période horaire d'occupation des bureaux est de",debuthoraire, "à",finhoraire)

