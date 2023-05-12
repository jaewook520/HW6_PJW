#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random as rand
import csv

def exe_rand(n, result):
    for i in range(n):
        result.append(rand.randrange(1,7))

def main():
    
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    
    f = open('random.csv','w',newline='')
    wr = csv.writer(f)
    wr.writerow(['100번 시행','1000번 시행','10000번 시행','100000번 시행'])
    exe_rand(100, result1)
    exe_rand(1000, result2)
    exe_rand(10000, result3)
    exe_rand(100000, result4)
    for i in range(100000):
        if i >= 0 and i < 100:
            wr.writerow([result1[i], result2[i], result3[i], result4[i]])
        elif i >= 100 and i < 1000:
            wr.writerow(['', result2[i], result3[i], result4[i]])
        elif i >= 1000 and i < 10000:
            wr.writerow(['', '', result3[i], result4[i]])
        else:
            wr.writerow(['','','', result4[i]])
    f.close()
    
if __name__=="__main__":
    main()

