#!/usr/bin/env python
# coding: utf-8

# In[17]:


import csv
import matplotlib.pyplot as plt
from itertools import islice

def main():
    f = open('subway.csv', 'r', encoding='ANSI')
    data = csv.reader(f)
    next(data)
    next(data)
    station_in = dict()
    station_out = dict()
    station_inout = dict()
    
    for row in data:
        station = row[3]
        station_in[station] = int(row[10]) + int(row[12])
        station_out[station] = int(row[11]) + int(row[13])
        station_inout[station] = int(row[10]) + int(row[11]) + int(row[12]) + int(row[13])
    
    f.close()
        
    station_in = dict(islice(sorted(station_in.items(), key=lambda x: x[1], reverse=True), 30))
    station_out = dict(islice(sorted(station_out.items(), key=lambda x: x[1], reverse=True), 30))
    station_inout = dict(islice(sorted(station_inout.items(), key=lambda x: x[1], reverse=True), 30))
    
    plt.rcParams['font.family']='Malgun Gothic'
    plt.rcParams['axes.unicode_minus']=False
    
    plt.figure(figsize=(18,20))
    
    plt.subplot(3,1,1)
    xdata = station_in.keys()
    ydata = station_in.values()
    plt.title('출근시간 최대 승차역 30개')
    plt.xlabel('station name')
    plt.ylabel('승차인원')
    plt.xticks(rotation=90)
    plt.bar(xdata, ydata)
    
    plt.subplot(3,1,2)
    xdata = station_out.keys()
    ydata = station_out.values()
    plt.title('출근시간 최대 하차역 30개')
    plt.xlabel('station name')
    plt.ylabel('하차인원')
    plt.xticks(rotation=90)
    plt.bar(xdata, ydata)
    
    plt.subplot(3,1,3)
    xdata = station_inout.keys()
    ydata = station_inout.values()
    plt.title('출근시간 최대 승하차역 30개')
    plt.xlabel('station name')
    plt.ylabel('승하차인원')
    plt.xticks(rotation=90)
    plt.bar(xdata, ydata)
    
    plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.6)
    
    plt.show()
    
if __name__=="__main__":
    main()


# In[ ]:




