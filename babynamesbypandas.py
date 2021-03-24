#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:53:46 2019

@author: lixi
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("baby-names-new.csv")


print(df.iloc[df["percent"].idxmax()])


fdf=df[df["percent"]==df["percent"].max()]
print(fdf.iloc[0]["name"])

a=df.percent.idxmax()
print(len(df))
print(df.shape[0])
print("Name", df.loc[a,"name"],"was given to",df.loc[a,"percent"],"in", df.loc[a,"year"] )
print(df["percent"].max())
g=input("Gender:")
s=input("Style: ")

fdf=df[df["sex"]==g]
if s=="classic":
    fdf=fdf[fdf["year"]<=1899 ]
    ma=fdf.nlargest(1,"percent")
    print("We recommend ", ma["name"])    
elif s=="modern":
    fdf=fdf[fdf["year"]>=1990 ]
    mi=fdf.percent.idxmax()
    print("We recommend ", fdf.loc[mi,"name"])
    
elif s=="none":
    name=fdf.percent.idxmax()
    print("We recommend ", fdf.loc[name,"name"])
    
        
na=input("name: ")
fdf=df[df["name"]==na] 
p=fdf.percent.idxmax()
print(na,"most popular in ", fdf.loc[p,"year"])
gen=input("gender: ")
fdf=fdf[fdf["sex"]==gen]
p=fdf.percent.idxmax()

print("we suggest ", fdf.loc[p,"name"])

name=input("name:")
fdf=df[df["name"]==name]
x=fdf.year
y=fdf.percent

plt.plot(x,y)
plt.show()



    
    