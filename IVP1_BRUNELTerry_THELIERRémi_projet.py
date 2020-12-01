# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
sentat=data["sent_at"].tolist()
idcapteur=data["id"].tolist()

#Projet 1, Partie 1

def Tri_date(sentat):
    n = len(sentat)
    for i in range(n-1):
        for j in range(0, n-i-1):    
            if sentat[j] > sentat[j+1] : 
                sentat[j], sentat[j+1] = sentat[j+1], sentat[j] 
                noise[j], noise[j+1] = noise[j+1], noise[j] 
                temperature[j], temperature[j+1] = temperature[j+1], temperature[j] 
                humidite[j], humidite[j+1] = humidite[j+1], humidite[j]
                luminosite[j], luminosite[j+1] = luminosite[j+1], luminosite[j] 
                co2[j], co2[j+1] = co2[j+1], co2[j]
                idcapteur[j], idcapteur[j+1] = idcapteur[j+1], idcapteur[j]
    return sentat

date=Tri_date(sentat)


time1=[]
time2=[]
time3=[]
time4=[]
time5=[]
time6=[]
for i in range(len(date)):
    if idcapteur[i]==1:
        time1.append(date[i])
    elif idcapteur[i]==2:
        time2.append(date[i])
    elif idcapteur[i]==3:
        time3.append(date[i])
    elif idcapteur[i]==4:
        time4.append(date[i])
    elif idcapteur[i]==5:
        time5.append(date[i])
    elif idcapteur[i]==6:
        time6.append(date[i])
        
cap1_temp=[]
cap1_hum=[]
cap1_lum=[]
cap1_noi=[]
cap1_co2=[]
for i in range(len(time1)):
    cap1_temp.append(temperature[i])
    cap1_hum.append(humidite[i])
    cap1_lum.append(luminosite[i])
    cap1_noi.append(noise[i])
    cap1_co2.append(co2[i])
    
cap2_temp=[]
cap2_hum=[]
cap2_lum=[]
cap2_noi=[]
cap2_co2=[]
for i in range(len(time2)):
    cap2_temp.append(temperature[i])
    cap2_hum.append(humidite[i])
    cap2_lum.append(luminosite[i])
    cap2_noi.append(noise[i])
    cap2_co2.append(co2[i])
    
cap3_temp=[]
cap3_hum=[]
cap3_lum=[]
cap3_noi=[]
cap3_co2=[]
for i in range(len(time3)):
    cap3_temp.append(temperature[i])
    cap3_hum.append(humidite[i])
    cap3_lum.append(luminosite[i])
    cap3_noi.append(noise[i])
    cap3_co2.append(co2[i])

cap4_temp=[]
cap4_hum=[]
cap4_lum=[]
cap4_noi=[]
cap4_co2=[]
for i in range(len(time4)):
    cap4_temp.append(temperature[i])
    cap4_hum.append(humidite[i])
    cap4_lum.append(luminosite[i])
    cap4_noi.append(noise[i])
    cap4_co2.append(co2[i])

cap5_temp=[]
cap5_hum=[]
cap5_lum=[]
cap5_noi=[]
cap5_co2=[]
for i in range(len(time5)):
    cap5_temp.append(temperature[i])
    cap5_hum.append(humidite[i])
    cap5_lum.append(luminosite[i])
    cap5_noi.append(noise[i])
    cap5_co2.append(co2[i])

cap6_temp=[]
cap6_hum=[]
cap6_lum=[]
cap6_noi=[]
cap6_co2=[]
for i in range(len(time6)):
    cap6_temp.append(temperature[i])
    cap6_hum.append(humidite[i])
    cap6_lum.append(luminosite[i])
    cap6_noi.append(noise[i])
    cap6_co2.append(co2[i])



    

def maxi(Y):
    maxi=Y[0]
    n=len(Y)
    for i in range(n):
        if Y[i]>=maxi:
            maxi=Y[i]
    return maxi

def mini(Y):
    mini=Y[0]
    n=len(Y)
    for i in range(n):
        if Y[i]<mini:
            mini=Y[i]
    return mini
    
def mediane(Y):
    n = len(Y)
    index = n // 2
    if n < 1:
        return None
    if n % 2:
         return sorted(Y)[index]
    return sum(sorted(Y)[index - 1:index + 1]) / 2

def moyenne(Y):
    mo=0
    n=len(Y)
    for k in Y:
        mo += k
    mo=mo/n
    moy=round(mo,2)
    return moy
    

def variance(Y):
    va=0
    moy=moyenne(Y)
    for i in Y:
        va=va+(i - moy)**2
    va= va/len(Y) 
    var=round(va,2)
    return var
    

def ecart_type(Y):
    ecar=variance(Y)**0.5
    ecart=round(ecar,2)
    return ecart  
       


def T_ros(temperature,humidite):
      T_ros=[]
      for i in range (0,len(temperature)):
           a=(17.27*temperature[i])/(237.7+temperature[i])+np.log(humidite[i]/100)
           T_ros.append((237.7*a)/(17.27-a))
      return T_ros


def humidex(T_ros):
     H=[]
     for i in range (0,len(temperature)):
          a=5417.7530*(1/273.16-1/(273.16+T_ros[i]))
          H.append(temperature[i]+0.5555*(6.11*np.exp(a)-10))
     return H

def SET_ros(SEtemperature,SEhumidite):
      SET_ros=[]
      for i in range (0,len(SEtemperature)):
           a=(17.27*SEtemperature[i])/(237.7+SEtemperature[i])+np.log(SEhumidite[i]/100)
           SET_ros.append((237.7*a)/(17.27-a))
      return SET_ros


def SEhumidex(SET_ros):
     SEH=[]
     for i in range (0,len(SEtemperature)):
          a=5417.7530*(1/273.16-1/(273.16+SET_ros[i]))
          SEH.append(temperature[i]+0.5555*(6.11*np.exp(a)-10))
     return SEH
        
        
def cov(X,Y):
    n=len(X)
    L=0
    M=0
    for i in range(n):
        L+=((X[i]-moyenne(X))*((Y[i]-moyenne(Y))))
        M=(L/n)
    return M

def correl(X,Y):
    r=cov(X,Y)/((variance(X)*variance(Y))**0.5)
    return r



        


rep0=str(input("Voulez-vous un intervalle de temps? (répondre par oui ou par non): "))
if rep0=="oui" or rep0=="Oui" or rep0=="Yes" or rep0=="yes" or rep0=="YES" or rep0=="OUI":
    print("les dates commencent du 2019-08-11 et terminent au 2019-08-25, veuillez choisir des dates comprises dans cet encadrement")
    debut=str(input('quelle date initiale souhaitez-vous? (AAAA-MM-JJ) :')) 
    fin=str(input('quelle date finale souhaitez-vous? (AAAA-MM-JJ) :'))

    debut=debut+'000000'
    fin=fin+'235959'

    start_date=int(debut[8:16])
    end_date=int(fin[8:16])
    

    def Newdate(date):
        newdate=[]
        for d in date:
            newdate.append(d[8:10]+d[11:13]+d[14:16]+d[17:19])
        return newdate

    newdate=Newdate(date)


    def indicestart(start_date):
        for i in range(len(newdate)):
           if start_date<=int(newdate[i]):
               return i
    
    def indiceend(end_date):
        for i in range(len(newdate)):
            if int(newdate[i])>end_date:
                return i
               
    SEnewdate=newdate[indicestart(start_date):indiceend(end_date)]  
    SEco2=co2[indicestart(start_date):indiceend(end_date)]
    SEluminosite=luminosite[indicestart(start_date):indiceend(end_date)]
    SEhumidite=humidite[indicestart(start_date):indiceend(end_date)]
    SEtemperature=temperature[indicestart(start_date):indiceend(end_date)]
    SEnoise=noise[indicestart(start_date):indiceend(end_date)]
    
    

    choix=str(input("Quelle donnée souhaitez-vous étudier? Choisissez entre bruit, température, humidité, luminosité, co2 : "))
    rep3=str(input("Voulez-vous observer l'évolution de l'indice humidex en fonction du temps? (Répondre par oui ou par non) : "))
    rep4=str(input("Voulez vous étudier la corrélation entre 2 variables? (répondre par oui ou par non) : "))
    
   
    if rep4=="Oui" or rep4=="oui" or rep4=="Yes" or rep4=="yes" or rep4=="OUI" or rep4=="YES":
        data_1=str(input('Quelle première donnée voulez vous étudier entre bruit, température, humidité, lumière et co2 pour calculer l indice de corélation ? ' ))
        if data_1 == "bruit" or data_1=="Bruit" or data_1=="noise" or data_1=="Noise" or data_1=="BRUIT" or data_1=="NOISE":
            data1=SEnoise
        if data_1== "température" or data_1=="temperature" or data_1=="Temperature" or data_1=="Température" or data_1=="TEMPERATURE":
            data1=SEtemperature
        if data_1 == "humidité" or data_1=="humidité" or data_1=="Humidite" or data_1=="Humidité" or data_1=="humidity" or data_1=="Humidity" or data_1=="HUMIDITE" or data_1=="HUMIDITY":
            data1=SEhumidite
        if data_1=="luminosite" or data_1=="luminosité" or data_1=="Luminosite" or data_1=="Luminosité" or data_1=="luminosity" or data_1=="Luminosity" or data_1=="LUMINOSITE" or data_1=="LUMINOSITY":
            data1=SEluminosite
        if data_1 =="co2" or data_1=="CO2" or data_1=="Co2":
            data1=SEco2
        data_2=str(input('Quelle seconde donnée voulez vous étudier entre bruit, température, humidité, lumière et co2 pour calculer l indice de corélation ? ' ))
        if data_2 == "bruit" or data_2=="Bruit" or data_2=="noise" or data_2=="Noise" or data_2=="BRUIT" or data_2=="NOISE":
            data2=SEnoise
        if data_2== "température" or data_2=="temperature" or data_2=="Temperature" or data_2=="Température" or data_2=="TEMPERATURE":
             data2=SEtemperature
        if data_2 == "humidité" or data_2=="humidite" or data_2=="Humidite" or data_2=="Humidité" or data_2=="humidity" or data_2=="Humidity" or data_2=="HUMIDITE" or data_2=="HUMIDITY":
            data2=SEhumidite
        if data_2=="luminosite" or data_2=="luminosité" or data_2=="Luminosite" or data_2=="Luminosité" or data_2=="luminosity" or data_2=="Luminosity" or data_2=="LUMINOSITE" or data_2=="LUMINOSITY":
            data2=SEluminosite
        if data_2 =="co2" or data_2=="CO2" or data_2=="Co2":
            data2=SEco2

    if choix=="température" or choix=="temperature" or choix=="Temperature" or choix=="Température" or choix=="TEMPERATURE":
        print("la température maximale en °C est",maxi(SEtemperature))
        print("la température minimale en °C est",mini(SEtemperature))
        print("la médiane  en °C de la liste de température est",mediane(SEtemperature))
        print("la moyenne en °C des températures est",moyenne(SEtemperature))
        print("la variance  en °C de la liste de température est",variance(SEtemperature))
        print("l'écart type de la liste de température est",ecart_type(SEtemperature))
       
        plt.plot(SEnewdate,SEtemperature,label="capteurs")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(SEtemperature),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(SEtemperature),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(SEtemperature),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(SEtemperature),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(SEtemperature),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(SEtemperature),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par les capteurs en fonction du temps")
        plt.show()
    elif choix=="humidite" or choix=="humidité" or choix=="Humidite" or choix=="Humidité" or choix=="humidity" or choix=="Humidity" or choix=="HUMIDITE" or choix=="HUMIDITY":
        print("l'humidité relative maximale est",maxi(SEhumidite))
        print("l'humidité relative minimale est",mini(SEhumidite))
        print("la médiane de la liste humidité relative est",mediane(SEhumidite))
        print("la moyenne de l'humidité relative est",moyenne(SEhumidite))
        print("la variance de la liste humidité relative est",variance(SEhumidite))
        print("l'écart type de la liste  humidité relative est",ecart_type(SEhumidite))
        
        plt.plot(SEnewdate,SEhumidite,label="capteurs")
        plt.annotate("maximum:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(SEhumidite),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(SEhumidite),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(SEhumidite),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(SEhumidite),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(SEhumidite),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(SEhumidite),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("Humidité relative (%) enregistrée par les capteurs en fonction du temps")
        plt.show()
    elif choix=="luminosite" or choix=="luminosité" or choix=="Luminosite" or choix=="Luminosité" or choix=="luminosity" or choix=="Luminosity" or choix=="LUMINOSITE" or choix=="LUMINOSITY":
        print("la luminosité maximale en Lux est",maxi(SEluminosite))
        print("la luminosité minimale en Lux est",mini(SEluminosite))
        print("la médiane en Lux de la liste luminosité est",mediane(SEluminosite))
        print("la moyenne en Lux des données luminosité est",moyenne(SEluminosite))
        print("la variance en Lux de la liste luminosité est",variance(SEluminosite))
        print("l'écart type en Lux de la liste luminosité est",ecart_type(SEluminosite))
       
        plt.plot(SEnewdate,SEluminosite,label="capteurs")
        plt.annotate("maximum [lux]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(SEluminosite),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(SEluminosite),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(SEluminosite),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(SEluminosite),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(SEluminosite),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(SEluminosite),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("Luminosité (lux) enregistrée par les capteurs en fonction du temps")
        plt.show()
    elif choix=="bruit" or choix=="Bruit" or choix=="noise" or choix=="Noise" or choix=="BRUIT" or choix=="NOISE":
        print("le niveau sonore maximal en dB est",maxi(SEnoise))
        print("le niveau sonore minimal en dB est",mini(SEnoise))
        print("la médiane en dB de la liste du niveau sonore est",mediane(SEnoise))
        print("la moyenne en dB du niveau sonore est",moyenne(SEnoise))
        print("la variance en dB de la liste du niveau sonore est",variance(SEnoise))
        print("l'écart type en dB de la liste du niveau snore est",ecart_type(SEnoise))
        
        plt.plot(SEnewdate,SEnoise,label="capteurs")
        plt.annotate("maximum [dB]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(SEnoise),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(SEnoise),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(SEnoise),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(SEnoise),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(SEnoise),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(SEnoise),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistrée par les capteurs en fonction du temps")
        plt.show()
    elif choix=="co2" or choix=="Co2" or choix=="CO2" :
        print("la quantité de CO2 maximale en ppm est",maxi(SEco2))
        print("la quantité minimale de CO2 en ppm est",mini(SEco2))
        print("la médiane en ppm de la liste CO2 est",mediane(SEco2))
        print("la moyenne en ppm de quantité de CO2 est",moyenne(SEco2))
        print("la variance en ppm de la liste CO2 est",variance(SEco2))
        print("l'écart type en ppm e la liste CO2 est",ecart_type(SEco2))
        
        plt.plot(SEnewdate,SEco2,label="capteurs")
        plt.annotate("maximum [ppm]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(SEco2),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(SEco2),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(SEco2),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(SEco2),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(SEco2),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(SEco2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("Quantité de CO2 (ppm) enregistrée par les capteurs en fonction du temps")
        plt.show()
    

    if rep3=="oui" or rep3=="Oui" or rep3=="Yes" or rep3=="yes" or rep3=="OUI" or rep3=="YES":
        plt.plot(SEnewdate,SEhumidex(SET_ros(SEtemperature,SEhumidite)),label='humidex')
        plt.xlabel('Temps')
        plt.ylabel('indice Humidex ')
        plt.legend()
        plt.title("indice humidex enregistré par tous les capteurs en fonction du temps")
        plt.show()



    if rep4=="oui" or rep4=="Oui" or rep4=="Yes" or rep4=="yes" or rep4=="OUI" or rep4=="YES":
        print("la donnée affichée en rouge correspond à la 1ère donnée demandée pour indice de corrélation") 
        print("la donnée affichée en bleu correspond à la 2ème donnée demande pour indice de corrélation")     
        plt.plot(SEnewdate,data1,'r--',label='1er donnée entrée')
        plt.plot(SEnewdate,data2,'b--',label='2ème donnée entrée')
        plt.xlabel("Temps")
        plt.ylabel("données")
        plt.annotate("indice de corrélation:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(correl(data1,data2),(1.35,0.6),xycoords="axes fraction")
        plt.title("Données entrées en fonction du temps pour calculer lindice de corrélation")
        plt.legend()
        plt.show()

else:
    print("les valeurs qui seront affichées commenceront du 2019-08-11 (début d'enregistrement des capteurs) au 2019-08-25 (fin d'enregistrement) ")

    choix=str(input("Quelle donnée souhaitez-vous étudier? Choisissez entre bruit, température, humidité, luminosité, co2 : "))
    rep1=str(input("Voulez-vous observer l'évolution de l'indice humidex en fonction du temps? (Répondre par oui ou par non) : "))
    rep2=str(input("Voulez vous étudier la corrélation entre 2 variables? (répondre par oui ou par non) : "))
    
    

    if rep2=="Oui" or rep2=="oui" or rep2=="Yes" or rep2=="yes" or rep2=="OUI" or rep2=="YES":
        data_1=str(input('Quelle première donnée voulez vous étudier entre bruit, température, humidité, lumière et co2 pour calculer l indice de corélation ? ' ))
        if data_1 == "bruit" or data_1=="Bruit" or data_1=="noise" or data_1=="Noise" or data_1=="BRUIT" or data_1=="NOISE":
            data1=noise
        if data_1== "température" or data_1=="temperature" or data_1=="Temperature" or data_1=="Température" or data_1=="TEMPERATURE":
            data1=temperature
        if data_1 == "humidité" or data_1=="humidité" or data_1=="Humidite" or data_1=="Humidité" or data_1=="humidity" or data_1=="Humidity" or data_1=="HUMIDITE" or data_1=="HUMIDITY":
            data1=humidite
        if data_1=="luminosite" or data_1=="luminosité" or data_1=="Luminosite" or data_1=="Luminosité" or data_1=="luminosity" or data_1=="Luminosity" or data_1=="LUMINOSITE" or data_1=="LUMINOSITY":
            data1=luminosite
        if data_1 =="co2" or data_1=="CO2" or data_1=="Co2":
            data1=co2
        data_2=str(input('Quelle seconde donnée voulez vous étudier entre bruit, température, humidité, lumière et co2 pour calculer l indice de corélation ? ' ))
        if data_2 == "bruit" or data_2=="Bruit" or data_2=="noise" or data_2=="Noise" or data_2=="BRUIT" or data_2=="NOISE":
            data2=noise
        if data_2== "température" or data_2=="temperature" or data_2=="Temperature" or data_2=="Température" or data_2=="TEMPERATURE":
            data2=temperature
        if data_2 == "humidité" or data_2=="humidité" or data_2=="Humidite" or data_2=="Humidité" or data_2=="humidity" or data_2=="Humidity" or data_2=="HUMIDITE" or data_2=="HUMIDITY":
            data2=humidite
        if data_2=="luminosite" or data_2=="luminosité" or data_2=="Luminosite" or data_2=="Luminosité" or data_2=="luminosity" or data_2=="Luminosity" or data_2=="LUMINOSITE" or data_2=="LUMINOSITY":
            data2=luminosite
        if data_2 =="co2" or data_2=="CO2" or data_2=="Co2":
            data2=co2

    if choix=="température" or choix=="temperature" or choix=="Temperature" or choix=="Température" or choix=="TEMPERATURE":
        print("la température maximale en °C est",maxi(temperature))
        print("la température minimale en °C est",mini(temperature))
        print("la médiane en °C de la liste de température est",mediane(temperature))
        print("la moyenne en °C des températures est",moyenne(temperature))
        print("la variance en °C de la liste de température est",variance(temperature))
        print("l'écart type en °C de la liste de température est",ecart_type(temperature))
        plt.plot(date,temperature,label="capteurs")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(temperature),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(temperature),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(temperature),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(temperature),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(temperature),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(temperature),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par les capteurs en fonction du temps")
        plt.show()
        plt.plot(time1,cap1_temp,label="capteur 1")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap1_temp),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap1_temp),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap1_temp),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap1_temp),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap1_temp),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap1_temp),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par le capteur 1 en fonction du temps")
        plt.show()
        plt.plot(time2,cap2_temp,label= "capteur 2")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap2_temp),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap2_temp),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap2_temp),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap2_temp),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap2_temp),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap2_temp),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par le capteur 2 en fonction du temps")
        plt.show()
        plt.plot(time3,cap3_temp,label= "capteur 3")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap3_temp),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap3_temp),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap3_temp),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap3_temp),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap3_temp),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap3_temp),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par le capteur 3 en fonction du temps")
        plt.show()
        plt.plot(time4,cap4_temp,label= "capteur 4")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap4_temp),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap4_temp),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap4_temp),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap4_temp),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap4_temp),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap4_temp),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par le capteur 4 en fonction du temps")
        plt.show()
        plt.plot(time5,cap5_temp,label= "capteur 5")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap5_temp),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap5_temp),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap5_temp),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap5_temp),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap5_temp),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap5_temp),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par le capteur 5 en fonction du temps")
        plt.show()
        plt.plot(time6,cap6_temp,label= "capteur 6")
        plt.annotate("maximum [°C]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap6_temp),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [°C]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap6_temp),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [°C]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap6_temp),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [°C]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap6_temp),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [°C]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap6_temp),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [°C]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap6_temp),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Température (°C)')
        plt.legend()
        plt.title("température (°C) enregistrée par le capteur 6 en fonction du temps")
        plt.show()
    elif choix=="humidite" or choix=="humidité" or choix=="Humidite" or choix=="Humidité" or choix=="humidity" or choix=="Humidity" or choix=="HUMIDITE" or choix=="HUMIDITY":
        print("l'humidité relative maximale est",maxi(humidite))
        print("l'humidité relative minimale est",mini(humidite))
        print("la médiane de la liste humidité relative est",mediane(humidite))
        print("la moyenne de l'humidité relative est",moyenne(humidite))
        print("la variance de la liste humidité relative est",variance(humidite))
        print("l'écart type de la liste  humidité relative est",ecart_type(humidite))
        plt.plot(date,humidite,label="capteurs")
        plt.annotate("maximum:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(humidite),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(humidite),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(humidite),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(humidite),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(humidite),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(humidite),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("Humidité relative (%) enregistrée par les capteurs en fonction du temps")
        plt.show()
        plt.plot(time1,cap1_hum,label='capteur 1')
        plt.annotate("maximum:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap1_hum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap1_hum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap1_hum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap1_hum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap1_hum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap1_hum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("humidité relative (%) enregistrée par le capteur 1 en fonction du temps")
        plt.show()
        plt.plot(time2,cap2_hum,label='capteur 2')
        plt.annotate("maximum:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap2_hum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap2_hum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap2_hum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap2_hum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap2_hum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap2_hum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("humidité relative (%) enregistrée par le capteur 2 en fonction du temps")
        plt.show()
        plt.plot(time3,cap3_hum,label='capteur 3')
        plt.annotate("maximum:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap3_hum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap3_hum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap3_hum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap3_hum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap3_hum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap3_hum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("humidité relative (%) enregistrée par le capteur 3 en fonction du temps")
        plt.show()
        plt.plot(time4,cap4_hum,label='capteur 4')
        plt.annotate("maximum:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap4_hum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap4_hum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap4_hum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap4_hum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap4_hum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap4_hum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("humidité relative (%) enregistrée par le capteur 4 en fonction du temps")
        plt.show()
        plt.plot(time5,cap5_hum,label='capteur 5')
        plt.annotate("maximum:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap5_hum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap5_hum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap5_hum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap5_hum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap5_hum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap5_hum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("humidité relative (%) enregistrée par le capteur 5 en fonction du temps")
        plt.show()
        plt.plot(time6,cap6_hum,label='capteur 6')
        plt.annotate("maximum:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap6_hum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap6_hum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap6_hum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap6_hum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap6_hum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap6_hum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Humidité relative (%)')
        plt.legend()
        plt.title("humidité relative (%) enregistrée par le capteur 6 en fonction du temps")
        plt.show()
    elif choix=="luminosite" or choix=="luminosité" or choix=="Luminosite" or choix=="Luminosité" or choix=="luminosity" or choix=="Luminosity" or choix=="LUMINOSITE" or choix=="LUMINOSITY":
        print("la luminosité maximale en lux est",maxi(luminosite))
        print("la luminosité minimale en lux est",mini(luminosite))
        print("la médiane en lux de la liste luminosité est",mediane(luminosite))
        print("la moyenne en luxdes luminosité est",moyenne(luminosite))
        print("la variance en lux de la liste luminosité est",variance(luminosite))
        print("l'écart type en lux de la liste luminosité est",ecart_type(luminosite))
        plt.plot(date,luminosite,label="capteurs")
        plt.annotate("maximum [lux]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(luminosite),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(luminosite),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(luminosite),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(luminosite),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(luminosite),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(luminosite),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("Luminosité (lux) enregistrée par les capteurs en fonction du temps")
        plt.show()
        plt.plot(time1,cap1_lum,label='capteur 1')
        plt.annotate("maximum [lux]:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap1_lum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap1_lum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap1_lum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap1_lum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap1_lum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap1_lum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("luminosité (lux) enregistrée par le capteur 1 en fonction du temps")
        plt.show()
        plt.plot(time2,cap2_lum,label='capteur 2')
        plt.annotate("maximum [lux]:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap2_lum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap2_lum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap2_lum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap2_lum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap2_lum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap2_lum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("luminosité (lux) enregistrée par le capteur 2 en fonction du temps")
        plt.show()
        plt.plot(time3,cap3_lum,label='capteur 3')
        plt.annotate("maximum [lux]:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap3_lum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap3_lum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap3_lum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap3_lum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap3_lum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap3_lum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("luminosité (lux) enregistrée par le capteur 3 en fonction du temps")
        plt.show()
        plt.plot(time4,cap4_lum,label='capteur 4')
        plt.annotate("maximum [lux]:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap4_lum),(1.20,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap4_lum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap4_lum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap4_lum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap4_lum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap4_lum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("luminosité (lux) enregistrée par le capteur 4 en fonction du temps")
        plt.show()
        plt.plot(time5,cap5_lum,label='capteur 5')
        plt.annotate("maximum [lux]:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap5_lum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap5_lum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap5_lum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap5_lum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap5_lum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap5_lum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("luminosité (lux) enregistrée par le capteur 5 en fonction du temps")
        plt.show()
        plt.plot(time6,cap6_lum,label='capteur 6')
        plt.annotate("maximum [lux]:",(1,0.8),xycoords="axes fraction")
        plt.annotate(maxi(cap6_lum),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [lux]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(cap6_lum),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [lux]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(cap6_lum),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [lux]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(cap6_lum),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [lux]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(cap6_lum),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [lux]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(cap6_lum),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Luminosité (lux)')
        plt.legend()
        plt.title("luminosité (lux) enregistrée par le capteur 6 en fonction du temps")
        plt.show()
    elif choix=="bruit" or choix=="Bruit" or choix=="noise" or choix=="Noise" or choix=="BRUIT" or choix=="NOISE":
        print("le niveau sonore maximal en dB est",maxi(noise))
        print("le niveau sonore minimal en dB est",mini(noise))
        print("la médiane en dB  de la liste du niveau sonore est",mediane(noise))
        print("la moyenne en dB du niveau sonore est",moyenne(noise))
        print("la variance en dB de la liste du niveau sonore est",variance(noise))
        print("l'écart type en dB de la liste du niveau snore est",ecart_type(noise))
        plt.plot(date,noise,label="capteurs")
        plt.annotate("maximum [dB]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(noise),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(noise),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(noise),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(noise),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(noise),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(noise),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistrée par les capteurs en fonction du temps")
        plt.show()
        plt.plot(time1,cap1_noi,label='capteur 1')
        plt.gca().annotate("maximum [dB]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap1_noi),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap1_noi),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap1_noi),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap1_noi),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap1_noi),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap1_noi),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistré par le capteur 1 en fonction du temps")
        plt.show()
        plt.plot(time2,cap2_noi,label='capteur 2')
        plt.gca().annotate("maximum [dB]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap2_noi),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap2_noi),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap2_noi),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap2_noi),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap2_noi),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap2_noi),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistré par le capteur 2 en fonction du temps")
        plt.show()
        plt.plot(time3,cap3_noi,label='capteur 3')
        plt.gca().annotate("maximum [dB]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap3_noi),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap3_noi),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap3_noi),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap3_noi),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap3_noi),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap3_noi),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistré par le capteur 3 en fonction du temps")
        plt.show()
        plt.plot(time4,cap4_noi,label='capteur 4')
        plt.gca().annotate("maximum [dB]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap4_noi),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap4_noi),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap4_noi),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap4_noi),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap4_noi),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type[dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap4_noi),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistré par le capteur 4 en fonction du temps")
        plt.show()
        plt.plot(time5,cap5_noi,label='capteur 5')
        plt.gca().annotate("maximum [dB]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap5_noi),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap5_noi),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap5_noi),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap5_noi),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap5_noi),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap5_noi),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistré par le capteur 5 en fonction du temps")
        plt.show()
        plt.plot(time6,cap6_noi,label='capteur 6')
        plt.gca().annotate("maximum [dB]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap6_noi),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [dB]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap6_noi),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [dB]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap6_noi),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [dB]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap6_noi),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [dB]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap6_noi),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [dB]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap6_noi),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Niveau sonore (dB)')
        plt.legend()
        plt.title("Niveau sonore (dB) enregistré par le capteur 6 en fonction du temps")
        plt.show()
    elif choix=="co2" or choix=="Co2" or choix=="CO2" :
        print("la quantité de CO2 maximale en ppm est",maxi(co2))
        print("la quantité minimale de CO2 en ppm est",mini(co2))
        print("la médiane en ppm de la liste CO2 est",mediane(co2))
        print("la moyenne en ppm de quantité de CO2 est",moyenne(co2))
        print("la variance en ppm de la liste CO2 est",variance(co2))
        print("l'écart type en ppm de la liste CO2 est",ecart_type(co2))
        plt.plot(date,co2,label="capteurs")
        plt.annotate("maximum [ppm]:",(1.0,0.8),xycoords="axes fraction")
        plt.annotate(maxi(co2),(1.30,0.8),xycoords="axes fraction")
        plt.annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.annotate(mini(co2),(1.30,0.7),xycoords="axes fraction")
        plt.annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(mediane(co2),(1.30,0.6),xycoords="axes fraction")
        plt.annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.annotate(moyenne(co2),(1.30,0.5),xycoords="axes fraction")
        plt.annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.annotate(variance(co2),(1.30,0.4),xycoords="axes fraction")
        plt.annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.annotate(ecart_type(co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("Quantité de CO2 (ppm) enregistrée par les capteurs en fonction du temps")
        plt.show()
        plt.plot(time1,cap1_co2,label='capteur 1')
        plt.gca().annotate("maximum [ppm]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap1_co2),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap1_co2),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap1_co2),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap1_co2),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap1_co2),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap1_co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("quantité de CO2 (ppm) enregistrée par le capteur 1 en fonction du temps")
        plt.show()
        plt.plot(time2,cap2_co2,label='capteur 2')
        plt.gca().annotate("maximum [ppm]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap2_co2),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap2_co2),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap2_co2),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap2_co2),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap2_co2),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap2_co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("quantité de CO2 (ppm) enregistrée par le capteur 2 en fonction du temps")
        plt.show()
        plt.plot(time3,cap3_co2,label='capteur 3')
        plt.gca().annotate("maximum [ppm]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap3_co2),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [ppm]",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap3_co2),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap3_co2),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap3_co2),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap3_co2),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap3_co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("quantité de CO2 (ppm) enregistrée par le capteur 3 en fonction du temps")
        plt.show()
        plt.plot(time4,cap4_co2,label='capteur 4')
        plt.gca().annotate("maximum [ppm]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap4_co2),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap4_co2),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap4_co2),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap4_co2),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap4_co2),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap4_co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("quantité de CO2 (ppm) enregistrée par le capteur 4 en fonction du temps")
        plt.show()
        plt.plot(time5,cap5_co2,label='capteur 5')
        plt.gca().annotate("maximum [ppm]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap5_co2),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap5_co2),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap5_co2),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap5_co2),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap5_co2),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap5_co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("quantité de CO2 (ppm) enregistrée par le capteur 5 en fonction du temps")
        plt.show()
        plt.plot(time6,cap6_co2,label='capteur 6')
        plt.gca().annotate("maximum [ppm]:",(1,0.8),xycoords="axes fraction")
        plt.gca().annotate(maxi(cap6_co2),(1.30,0.8),xycoords="axes fraction")
        plt.gca().annotate("minimum [ppm]:",(1.0,0.7),xycoords="axes fraction")
        plt.gca().annotate(mini(cap6_co2),(1.30,0.7),xycoords="axes fraction")
        plt.gca().annotate("mediane [ppm]:",(1.0,0.6),xycoords="axes fraction")
        plt.gca().annotate(mediane(cap6_co2),(1.30,0.6),xycoords="axes fraction")
        plt.gca().annotate("moyenne [ppm]:",(1.0,0.5),xycoords="axes fraction")
        plt.gca().annotate(moyenne(cap6_co2),(1.30,0.5),xycoords="axes fraction")
        plt.gca().annotate("variance [ppm]:",(1.0,0.4),xycoords="axes fraction")
        plt.gca().annotate(variance(cap6_co2),(1.30,0.4),xycoords="axes fraction")
        plt.gca().annotate("écart-type [ppm]:",(1.0,0.3),xycoords="axes fraction")
        plt.gca().annotate(ecart_type(cap6_co2),(1.30,0.3),xycoords="axes fraction")
        plt.xlabel('Temps')
        plt.ylabel('Quantité de CO2 (ppm)')
        plt.legend()
        plt.title("quantité de CO2 (ppm) enregistrée par le capteur 6 en fonction du temps")
        plt.show()
    

    if rep1=="oui" or rep1=="Oui" or rep1=="Yes" or rep1=="yes" or rep1=="OUI" or rep1=="YES":
        plt.plot(date,humidex(T_ros(temperature,humidite)),label='humidex')
        plt.xlabel('Temps')
        plt.ylabel('indice Humidex ')
        plt.legend()
        plt.title("indice humidex enregistré par tous les capteurs en fonction du temps")
        plt.show()
        


    if rep2=="oui" or rep2=="Oui" or rep2=="Yes" or rep2=="yes" or rep2=="OUI" or rep2=="YES":
        print("la donnée affichée en rouge correspond à la 1ère donnée demandée pour indice de corrélation") 
        print("la donnée affichée en bleu correspond à la 2ème donnée demande pour indice de corrélation")     
        plt.plot(date,data1,'r--',label='1er donnée entrée')
        plt.plot(date,data2,'b--',label='2ème donnée entrée')
        plt.xlabel("Temps")
        plt.ylabel("données")
        plt.annotate("indice de corrélation:",(1.0,0.6),xycoords="axes fraction")
        plt.annotate(correl(data1,data2),(1.35,0.6),xycoords="axes fraction")
        plt.title("Données entrées (pour calcul de lindice de corrélation) en fonction du temps")
        plt.legend()
        plt.show()
        
        
        
#Projet 1, Partie 2

    
def anomalies(liste):
    
    if choi== "bruit" or choi=="Bruit" or choi=="noise" or choi=="Noise" or choi=="BRUIT" or choi=="NOISE":
        larg=5
        pres=0.5
        liste=noise
    if choi=="température" or choi=="temperature" or choi=="Temperature" or choi=="Température" or choi=="TEMPERATURE":
        larg=10
        pres=0.8
        liste=temperature
    if choi=="luminosite" or choi=="luminosité" or choi=="Luminosite" or choi=="Luminosité" or choi=="luminosity" or choi=="Luminosity" or choi=="LUMINOSITE" or choi=="LUMINOSITY":
        larg=3
        pres=0.99
        liste=luminosite
    if choi=="humidite" or choi=="humidité" or choi=="Humidite" or choi=="Humidité" or choi=="humidity" or choi=="Humidity" or choi=="HUMIDITE" or choi=="HUMIDITY":
        larg=10
        pres=0.8
        liste=humidite
    if choi=="co2" or choi=="Co2" or choi=="CO2" :
        larg= 10
        pres= 0.3
        liste=co2
    Ano=[]
    DateAno=[]
    for i in range (len(liste)):
        LG=[]
        LD=[]
        for k in range (1, larg):  #largeur
            if (i-k>-1):
                LG.append(liste[i-k])  
            if (i+k<len(liste)):
                LD.append(liste[i+k])
        S=0
        C=LG+LD
        for j in range (len(C)):
            S=S+C[j]
        Moy=S/len(C)
        if (liste[i]<Moy*(1-pres)) or (liste[i]>(1+pres)*Moy):   #precision
            Ano.append(liste[i])
            DateAno.append(date[i])
    return Ano,DateAno

def problem (date):
    espace_temps=[]    #temps en minute
    date_anomalies=[]
    for i in range (len(date)-1):
        
        j1=int(date[i][8]+date[i][9])
        j2=int(date[i+1][8]+date[i+1][9])
        
        h1=int(date[i][11]+date[i][12])
        h2=int(date[i+1][11]+date[i+1][12])
        
        m1=int(date[i][14]+date[i][15])
        m2=int(date[i+1][14]+date[i+1][15])
        
        if j2-j1==0 :
            
            if h2-h1==0:
                espace_temps.append(m2-m1)
            else:
                w=60-m1+m2+(h2-h1-1)*60
                espace_temps.append(w)
        else:
            w=60-m1+m2
            espace_temps.append(w)
    anomalies_temps=[]
    for i in range (len(espace_temps)):
        if espace_temps[i]>9:
            anomalies_temps.append(espace_temps[i])
    for i in range (len(anomalies_temps)):
        date_anomalies.append([date[i],date[i+1]])
    return anomalies_temps, len (anomalies_temps), date_anomalies

anom=str(input("Voulez-vous étudier les anomalies d'une liste de données? (Oui ou Non) "))
if anom=="oui" or anom=="Oui" or anom=="Yes" or anom=="yes" or anom=="YES" or anom=="OUI":
    choi=str(input("De quelles données voulez vous étudier les anomalies? (faites 1 choix entre température, bruit, humidite, co2, luminosite) : "))
    if choi=="température" or choi=="temperature" or choi=="Temperature" or choi=="Température" or choi=="TEMPERATURE":
        print("les anomalies valeurs extrêmes de la liste sont:",anomalies(temperature))
        print("Le nombre d'anomalies est de:",len(anomalies(temperature)[0]))
    elif choi=="humidite" or choi=="humidité" or choi=="Humidite" or choi=="Humidité" or choi=="humidity" or choi=="Humidity" or choi=="HUMIDITE" or choi=="HUMIDITY":
        print("les anomalies valeurs extrêmes de la liste sont:",anomalies(humidite))
        print("Le nombre d'anomalies est de:",len(anomalies(humidite)[0]))
    elif choi=="luminosite" or choi=="luminosité" or choi=="Luminosite" or choi=="Luminosité" or choi=="luminosity" or choi=="Luminosity" or choi=="LUMINOSITE" or choi=="LUMINOSITY":
        print("les anomalies valeurs extrêmes de la liste sont:",anomalies(luminosite))
        print("Le nombre d'anomalies est de:",len(anomalies(luminosite)[0]))
    elif choi=="bruit" or choi=="Bruit" or choi=="noise" or choi=="Noise" or choi=="BRUIT" or choi=="NOISE":
        print("les anomalies valeurs extrêmes de la liste sont:",anomalies(noise))
        print("Le nombre d'anomalies est de:",len(anomalies(noise)[0]))
    elif choi=="co2" or choi=="Co2" or choi=="CO2" :
        print("les anomalies valeurs extrêmes de la liste sont:",anomalies(co2))
        print("Le nombre d'anomalies est de:",len(anomalies(co2)[0]))

print("Les anomalies d'intervalle de temps entre capteur sont:",problem(date)[0],"\n leurs dates correspondantes sont:",problem(date)[2],"\n le nombre d'anomalie est de :",problem(date)[1])

dateanom=anomalies(noise)
     
def occup_bureau(noise):
    occ_bureau=[]
    for i in range(len(noise)):
        if noise[i]>40 and luminosite[i]>200 :
            occ_bureau.append(date[i])
    return occ_bureau

ocbu=occup_bureau(noise)


def nonoccup_bureau(noise):
    nonocc_bureau=[]
    for i in range(len(noise)):
        if noise[i]<=40 and luminosite[i]<=200:
            nonocc_bureau.append(date[i])
    return nonocc_bureau

nocbu=nonoccup_bureau(noise)


def chiffrage(ocbu):
    c=[]
    for i in range(len(ocbu)):
        c.append(str(ocbu[i]))
    return c

c=chiffrage(ocbu)


def chiff(c):
    chif=[]
    for i in range(len(c)):
        for j in range(len(c[i])):
            chif.append(c[i][11:13]+c[i][14:16]+c[i][17:19])
    
    return  chif
ch=chiff(c)


debhor=min(ch)
finhor=max(ch)
debhora=str(debhor)
finhora=str(finhor)
debuthoraire=debhora[0:2]+":"+debhora[2:4]+":"+debhora[4:6]
finhoraire=finhora[0:2]+":"+finhora[2:4]+":"+finhora[4:6]
print("la période horaire d'occupation des bureaux est de",debuthoraire, "à",finhoraire)

    

 

    
