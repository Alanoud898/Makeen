#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from numpy.random import randn
import pandas as pd
from  scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


data= pd.read_csv("Weather2.csv")
data


# In[20]:


sns.boxplot(x="AirQuality",y="Tmean",data=data,linewidth=1.5)


# In[14]:


sns.pairplot(data)


# In[16]:


# lmplot():
sns.lmplot(x='RH',y='Tmean', data=data)


# In[13]:


sns.lmplot(x='RH',y='Tmean', data=data,ci=95)


# In[18]:


stats.linregress(data['RH'],data['Tmean'])


# In[21]:


#regiression line
slope, intercept, r_value, p_value, std_err = stats.linregress(data['year'],data['AirQuality'])
print("y="+str(np.round(slope,2))+"x+"+str(np.round(intercept,2)))


# In[24]:


stats.pearsonr(data['RH'],data['Tmean'])


# In[25]:


sns.residplot(data=data,x='RH',y='Tmean')
plt.show


# In[ ]:




