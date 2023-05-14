#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
import matplotlib.pyplot as plt

def main():
    f = [[],[],[],[],[]]
    month_temp_avg = [[0 for col in range(12)] for row in range(5)]
    
    f[0] = open('all.csv', 'r')
    f[1] = open('seoul.csv', 'r')
    f[2] = open('daejeon.csv', 'r')
    f[3] = open('busan.csv', 'r')
    f[4] = open('jeju.csv', 'r')
    
    for i in range(5):
        data = csv.reader(f[i])
        next(data)
        month = [[],[],[],[],[],[],[],[],[],[],[],[]]
        for row in data:
            month[int(row[0].split('-')[1])-1].append(float(row[2]))
        for j in range(12):
            month_temp_avg[i][j] = sum(month[j]) / len(month[j])
        f[i].close()
    
    plt.figure(figsize=(10,20))
    
    plt.subplot(2,1,1)
    plt.plot(range(1,13), month_temp_avg[0], label = 'all')
    plt.plot(range(1,13), month_temp_avg[1], label = 'seoul')
    plt.plot(range(1,13), month_temp_avg[2], label = 'daejeon')
    plt.plot(range(1,13), month_temp_avg[3], label = 'busan')
    plt.plot(range(1,13), month_temp_avg[4], label = 'jeju')
    plt.xticks(range(1,13))
    plt.xlabel('month')
    plt.ylabel('Temperature(C)')
    plt.legend()
    plt.title('2022 average monthly temperature')
    plt.grid(True, lw=0.4, ls='--')
    plt.show()
    
    plt.figure(figsize=(8,10))
    plt.subplot(2,1,2)
    for i in range(1, 5):
        temp_diff = []
        for j in range(12):
            temp_diff.append(month_temp_avg[i][j] - month_temp_avg[0][j])
        if i== 1: plt.plot(range(1,13), temp_diff, label='seoul-all')
        if i== 2: plt.plot(range(1,13), temp_diff, label='daejeon-all')
        if i== 3: plt.plot(range(1,13), temp_diff, label='busan-all')
        if i== 4: plt.plot(range(1,13), temp_diff, label='jeju-all')
    plt.xticks(range(1,13))
    plt.xlabel('month')
    plt.ylabel('Temperature(C) difference')
    plt.legend()
    plt.grid(True, lw=0.4, ls='--')
    plt.show()
    
if __name__=="__main__":
    main()


# In[ ]:




