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
sur_t=np.load('surf_time.npy')
sur_tem=np.load('surf_temp.npy')
w_t=np.load('wind_time.npy')
w_u=np.load('wind_u.npy')
turt_t_n=np.load('tuttle_time_num.npy')
tuttle_time_u=np.load('tuttle_time_u.npy')

for a in np.arange(len(sur_t)):
    if sur_tem[a]<=10:
        print 'a',a
        break
plt.figure(figsize=(10,5))
plt.plot(sur_t,sur_tem)
plt.plot([sur_t[0],sur_t[-1]],[10,10])
plt.show()
t=sur_t[a]
print 't',t

num=[]
time=[]

for a in np.arange(len(turt_t_n)):
    if turt_t_n[a]>t:
        time.append(turt_t_n[a])
        num.append(tuttle_time_u[a])
numx=[]
timex=[]
jian=3
for a in np.arange((time[0]-time[-1]).days/jian):
    timex.append(time[-1]+timedelta(days=jian*a))
for a in np.arange(len(timex)):
    nn=0
    
    for b in np.arange(len(time)):
        if time[b]>=timex[a] and time[b]<time[a]+timedelta(days=jian):
            nn=nn+num[b]
    
    numx.append(nn)
            
wind=[]
for a in np.arange(len(timex)):
    w=0
    for b in np.arange(len(w_t)):
        if w_t[b]>=timex[a] and w_t[b]<time[a]+timedelta(days=jian):
        #if w_t[b]>=time[a] and w_t[b]<time[a]+timedelta(hours=24*jian):
            w=w+w_u[b]
    wind.append(w)
plt.scatter(wind,numx)

X=wind
Y=numx
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print z1  #[ 1.          1.49333333]
print p1  # 1 x + 1.493
xx=np.linspace(-10,90,100)
yy=[]
for a in np.arange(len(xx)):
    yy.append(xx[a]*p1[1]+p1[0])
plt.plot(xx,yy)
plt.text(0,80,'r^2=%s'%str(np.corrcoef(wind,numx)[0][1]))
plt.xlabel('windstrss(pa)')
plt.ylabel('number( per day)')
plt.savefig('corrx',dpi=300)

np.save('2014windu',wind)

np.save('2014numu',numx)

np.save('2014xxu',xx)

np.save('2014yyu',yy)
    
            
    