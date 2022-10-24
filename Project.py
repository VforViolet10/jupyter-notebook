#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
fw=open("app.csv","w",newline="")
writepen=csv.writer(fw)
data=['age','sex','cp','trtbps','chol','fbs','restecg','thalachh','exng','oldpeak','slp','caa','thall']
writepen.writerow(data)
while True:
    age=int(input("Enter your age: "))
    sex=int(input("Enter your sex(female=0/male=1): "))
    cp=int(input())
    trtbps=int(input())
    chol=int(input())
    fbs=int(input("Is your fasting blood sugar > 120 mg/dl(True=1/False=0)?"))
    restecg=int(input())
    thalachh=int(input("maximum heart rate achieved"))
    exng=int(input("exercise induced angina(yes=1/no=0)"))
    oldpeak=float(input())
    slp=int(input())
    caa=int(input())
    thall=int(input("thallium stress result"))
    data=[age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall]
    writepen.writerow(data)
    a=input("Do you want to check other heart status(yes/no)?")
    if a=='yes':
        continue
    else:
        break
fw.close()


# In[ ]:




