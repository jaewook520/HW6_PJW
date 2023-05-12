#!/usr/bin/env python
# coding: utf-8

# In[53]:


import csv
import matplotlib.pyplot as plt

def main():
    f = open('random.csv','r')
    data = csv.reader(f, delimiter=',')
    next(data)
    result = [[],[],[],[]]
    for row in data:
        if(row[0] != ''):
            result[0].append(int(row[0]))
        if(row[1] != ''):
            result[1].append(int(row[1]))
        if(row[2] != ''):
            result[2].append(int(row[2]))
        if(row[3] != ''):
            result[3].append(int(row[3]))
    f.close()
    
    plt.rcParams['font.family']='Malgun Gothic'
    plt.rcParams['axes.unicode_minus']=False
    
    plt.figure(figsize=(6,20))
    
    plt.subplot(4,1,1)
    plt.title('주사위 100번 시행 결과')
    plt.xlabel('주사위 눈금')
    plt.ylabel('나온 횟수')
    plt.hist(result[0], bins=6, color='r', label='100번 시행', histtype='bar')
    plt.legend()
    
    plt.subplot(4,1,2)
    plt.title('주사위 1000번 시행 결과')
    plt.xlabel('주사위 눈금')
    plt.ylabel('나온 횟수')
    plt.hist(result[1], bins=6,  color='g', label='1000번 시행')
    plt.legend()
    
    plt.subplot(4,1,3)
    plt.title('주사위 10000번 시행 결과')
    plt.xlabel('주사위 눈금')
    plt.ylabel('나온 횟수')
    plt.hist(result[2], bins=6,  color='b', label='10000번 시행')
    plt.legend()
    
    plt.subplot(4,1,4)
    plt.title('주사위 100000번 시행 결과')
    plt.xlabel('주사위 눈금')
    plt.ylabel('나온 횟수')
    plt.hist(result[3], bins=6,  color='y', label='100000번 시행')
    plt.legend()
    
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




