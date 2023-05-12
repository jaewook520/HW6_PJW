#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import matplotlib.pyplot as plt

def main():
    f = []
    f.append(open('2010.csv','r', encoding='ANSI'))
    f.append(open('2013.csv','r', encoding='ANSI'))
    f.append(open('2016.csv','r', encoding='ANSI'))
    f.append(open('2019.csv','r', encoding='ANSI'))
    f.append(open('2022.csv','r', encoding='ANSI'))
    
    male = []
    female = []
    
    for i in range(5):
        data = csv.reader(f[i])
        next(data)
        row = next(data)
        male.append(int(row[2]))
        female.append(int(row[15]))
        f[i].close()
    xdata = [2010, 2013, 2016, 2019, 2022]
    
    plt.figure(figsize=(10,10))
    plt.rcParams['font.family']='Malgun Gothic'
    plt.rcParams['axes.unicode_minus']=False
    plt.xlabel('year')
    plt.ylabel('population')
    plt.title('제주도 남여 비율 비교 그래프')
    plt.plot(xdata, male, 'b.', label='male')
    plt.plot(xdata, female, 'r.', label='female')
    plt.legend()
    plt.xticks(xdata)
    plt.grid(True, lw=0.4, ls='--')
    plt.show()
    
if __name__=="__main__":
    main()


# In[ ]:




