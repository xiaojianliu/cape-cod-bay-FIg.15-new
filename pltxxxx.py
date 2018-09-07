# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 23:26:47 2017

@author: xiaojian
"""

import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import csv

windv2012=np.load('2012windv.npy')
numv2012=np.load('2012numv.npy')
xxv2012=np.load('2012xxv.npy')
yyv2012=np.load('2012yyv.npy')

windu2012=np.load('2012windu.npy')
numu2012=np.load('2012numu.npy')
xxu2012=np.load('2012xxu.npy')
yyu2012=np.load('2012yyu.npy')

windv2013=np.load('2013windv.npy')
numv2013=np.load('2013numv.npy')
xxv2013=np.load('2013xxv.npy')
yyv2013=np.load('2013yyv.npy')

windu2013=np.load('2013windu.npy')
numu2013=np.load('2013numu.npy')
xxu2013=np.load('2013xxu.npy')
yyu2013=np.load('2013yyu.npy')

windv2014=np.load('2014windv.npy')
numv2014=np.load('2014numv.npy')
xxv2014=np.load('2014xxv.npy')
yyv2014=np.load('2014yyv.npy')

windu2014=np.load('2014windu.npy')
numu2014=np.load('2014numu.npy')
xxu2014=np.load('2014xxu.npy')
yyu2014=np.load('2014yyu.npy')

fig,axes=plt.subplots(4,2,figsize=(12,10))
plt.subplots_adjust(wspace=0.1,hspace=0.2)

axes[0,0].scatter(windu2012,numu2012)
axes[0,1].scatter(-np.array(windv2012),numv2012)
axes[1,0].scatter(windu2013,numu2013)
axes[1,1].scatter(-np.array(windv2013),numv2013)
####################################################################
'''
X=wu
Y=nu
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1

xx=np.linspace(-20,80,100)
yy=[]
for a in np.arange(len(xx)):
    yy.append(xx[a]*p1[1]+p1[0])
'''
X=-np.array(windv2012)
Y=numv2012
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
xx1=np.linspace(-5,50,100)
yy1=[]
for a in np.arange(len(xx1)):
    yy1.append(xx1[a]*p1[1]+p1[0])
######################################################3

axes[0,0].plot(xxu2012,yyu2012)
axes[0,1].plot(xx1,yy1)
#axes[0,1].plot(xxv2012,yyv2012)
################################################33
X=-np.array(windv2013)
Y=numv2013
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
xx1=np.linspace(-5,50,100)
yy1=[]
for a in np.arange(len(xx1)):
    yy1.append(xx1[a]*p1[1]+p1[0])
########################################################3333
axes[1,0].plot(xxu2013,yyu2013)
axes[1,1].plot(xx1,yy1)
#########################################################
X=-np.array(windv2014)
Y=numv2014
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
xx1=np.linspace(-5,50,100)
yy1=[]
for a in np.arange(len(xx1)):
    yy1.append(xx1[a]*p1[1]+p1[0])
#####################################################
axes[2,0].scatter(windu2014,numu2014)
axes[2,1].scatter(-np.array(windv2014),numv2014)
'''
axes[,0].scatter(windu2013,numu2013)
axes[1,1].scatter(windv2013,numv2013)
'''

axes[2,0].plot(xxu2014,yyu2014)
axes[2,1].plot(xx1,yy1)
'''
axes[1,0].plot(xxu2013,yyu2013)
axes[1,1].plot(xxv2013,yyv2013)
'''

axes[0,0].text(70,300,'2012',fontsize=15)
axes[0,1].text(25,300,'2012',fontsize=15)
axes[1,0].text(70,300,'2013',fontsize=15)
axes[1,1].text(25,300,'2013',fontsize=15)

axes[2,0].text(70,300,'2014',fontsize=15)
axes[2,1].text(25,300,'2014',fontsize=15)

axes[3,0].text(40,300,'mean(2012-2014)',fontsize=15)
axes[3,1].text(20,300,'mean(2012-2014)',fontsize=15)

axes[0,0].text(70,200,'r^2=%s'%str(np.round(np.corrcoef(windu2012,numu2012)[0][1],2)),fontsize=12)
axes[0,1].text(25,200,'r^2=%s'%str(np.round(np.corrcoef(-np.array(windv2012),numv2012)[0][1],2)),fontsize=12)
axes[1,0].text(70,200,'r^2=%s'%str(np.round(np.corrcoef(windu2013,numu2013)[0][1],2)),fontsize=12)
axes[1,1].text(25,200,'r^2=%s'%str(np.round(np.corrcoef(-np.array(windv2013),numv2013)[0][1],2)),fontsize=12)

axes[2,0].text(70,200,'r^2=%s'%str(np.round(np.corrcoef(windu2014,numu2014)[0][1],2)),fontsize=12)
axes[2,1].text(25,200,'r^2=%s'%str(np.round(np.corrcoef(-np.array(windv2014),numv2014)[0][1],2)),fontsize=12)

'''
axes[0,0].set_xlabel('(a) sum of eastward wind stress per 3 days (pa)')
axes[0,1].set_xlabel('(b) sum of northward wind stress per 3 days (pa)')
axes[1,0].set_xlabel('(c) sum of eastward wind stress per 3 days (pa)')
axes[1,1].set_xlabel('(d) sum of northward wind stress per 3 days (pa)')

axes[2,0].set_xlabel('(e) sum of eastward wind stress per 3 days (pa)')
axes[2,1].set_xlabel('(f) sum of northward wind stress per 3 days (pa)')
'''
'''
axes[0,0].set_ylabel('the number of strandings (per 3 days)')
#axes[0,1].set_ylabel('the number of strandings (per 3 days)')
axes[1,0].set_ylabel('the number of strandings (per 3 days)')
#axes[1,1].set_ylabel('the number of strandings (per 3 days)')

axes[2,0].set_ylabel('the number of strandings (per 3 days)')
'''
axes[1,0].set_ylabel('the number of strandings (per 3 days)',fontsize=15)


axes[0,0].set_title('strandings vs eastward wind stress',fontsize=15)#Eastward wind stress vs strandings on Outer Cape towns')
axes[0,1].set_title('strandings vs northward wind stress',fontsize=15)#'Northward wind stress vs strandings on Mid Cape towns')
'''
axes[1,0].set_title('2013 eastward wind stress vs strandings on Outer Cape towns')
axes[1,1].set_title('2013 northward wind stress vs strandings on Upper Cape towns')

axes[2,0].set_title('2014 eastward wind stress vs strandings on Outer Cape towns')
axes[2,1].set_title('2014 northward wind stress vs strandings on Upper Cape towns')
'''
#plt.xlabel('windstrss(pa)')
#plt.ylabel('number( per day)')

wu=[]
wv=[]
nu=[]
nv=[]
for a in np.arange(len(windu2012)):
    wu.append(windu2012[a])
    nu.append(numu2012[a])
for a in np.arange(len(windu2013)):
    wu.append(windu2013[a])
    nu.append(numu2013[a])
for a in np.arange(len(windu2014)):
    wu.append(windu2014[a])
    nu.append(numu2014[a])
for a in np.arange(len(windv2012)):
    wv.append(windv2012[a])
    nv.append(numv2012[a])
for a in np.arange(len(windv2013)):
    wv.append(windv2013[a])
    nv.append(numv2013[a])

for a in np.arange(len(windv2014)):
    wv.append(windv2014[a])
    nv.append(numv2014[a])

X=wu
Y=nu
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
'''
plt.figure()
plt.scatter(wu,nu)   
'''
xx=np.linspace(-20,80,100)
yy=[]
for a in np.arange(len(xx)):
    yy.append(xx[a]*p1[1]+p1[0])
X=-np.array(wv)
Y=nv
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
xx1=np.linspace(-5,50,100)
yy1=[]
for a in np.arange(len(xx)):
    yy1.append(xx1[a]*p1[1]+p1[0])
'''
plt.figure()
plt.scatter(wv,nv)  
'''
'''
fig,axes=plt.subplots(1,2,figsize=(18,5))
plt.subplots_adjust(wspace=0.2,hspace=0.4)
'''
axes[3,0].scatter(wu,nu)  
axes[3,1].scatter(-np.array(wv),nv) 
axes[3,0].plot(xx,yy)
axes[3,1].plot(xx1,yy1)
axes[3,0].text(70,200,'r^2=%s'%str(np.round(np.corrcoef(wu,nu)[0][1],2)),fontsize=12)
axes[3,1].text(25,200,'r^2=%s'%str(np.round(np.corrcoef(-np.array(wv),nv)[0][1],2)),fontsize=12)

axes[3,0].set_xlabel('sum of eastward wind stress per 3 days (pa)',fontsize=12)
axes[3,1].set_xlabel('sum of northward wind stress per 3 days (pa)',fontsize=12)
'''
axes[3,0].set_title('mean eastward wind stress vs strandings on Outer Cape towns(2012-2014) ')
axes[3,1].set_title('mean northward wind stress vs strandings on Upper Cape towns(2012-2014)')
'''
###################################################################
#axes[0,1].xaxis.tick_top() 
axes[0,0].set_xticklabels([])

axes[1,0].set_xticklabels([])

axes[2,0].set_xticklabels([])

#axes[0,0].set_xticklabels([])
axes[0,1].set_yticklabels([])
axes[0,1].set_xticklabels([])

axes[1,1].set_yticklabels([])
axes[1,1].set_xticklabels([])

axes[2,1].set_yticklabels([])
axes[2,1].set_xticklabels([])

axes[3,1].set_yticklabels([])
#axes[3,1].set_xticklabels([])

axes[0,0].set_xlim([-20,100])
axes[1,0].set_xlim([-20,100])
axes[2,0].set_xlim([-20,100])
axes[3,0].set_xlim([-20,100])

axes[0,1].set_xlim([-10,50])
axes[1,1].set_xlim([-10,50])
axes[2,1].set_xlim([-10,50])
axes[3,1].set_xlim([-10,50])

axes[0,0].set_ylim([-200,400])
axes[1,0].set_ylim([-200,400])
axes[2,0].set_ylim([-200,470])
axes[3,0].set_ylim([-200,400])

axes[0,1].set_ylim([-200,400])
axes[1,1].set_ylim([-200,400])
axes[2,1].set_ylim([-200,470])
axes[3,1].set_ylim([-200,400])

plt.savefig('Fig15.eps',format='eps',dpi=300,bbox_inches='tight')

    
    