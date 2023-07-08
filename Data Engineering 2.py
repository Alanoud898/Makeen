#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[16]:


df = sns.load_dataset('tips')
df.head()


# In[21]:


# creat bar plot:

plt.figure(figsize=(8, 6))
sns.barplot(x='sex', y='tip', data=df)
plt.title('tip vs sex')
plt.xlabel('sex')
plt.ylabel('tip')
plt.show()


# In[19]:


# Create a scatter plot:
plt.figure(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=df)
plt.title('Total Bill Amount vs. Tip Amount')
plt.xlabel('Total Bill Amount')
plt.ylabel('Tip Amount')
plt.show()


# In[23]:


# Create a box plot:
plt.figure(figsize=(8, 6))
sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Tip Amount vs Amount by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Tip Amount')
plt.show()


# In[24]:


# Create a strip plot:
plt.figure(figsize=(8, 6))
sns.stripplot(x='time', y='tip', data=df)
plt.title('Time vs Tip')
plt.xlabel('time')
plt.ylabel('tip')
plt.show()


# In[ ]:




