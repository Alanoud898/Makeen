#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
from pandas import Series,DataFrame


# In[13]:



data = Series([9,8,100,12])


# In[14]:


data


# In[16]:


data.values


# In[17]:


data.index


# In[19]:


M= Series([22,55,66,88],index=['A','B','C','D'])


# m

# In[21]:


M


# In[22]:


M['D']


# In[23]:


M[M<67]


# In[24]:


M.D


# In[26]:


'A' in M


# In[27]:


'W' in M


# In[36]:


M= M.to_dict()


# In[35]:


M


# In[37]:


M_Series = Series(M)


# In[38]:


M_Series


# In[42]:


countries=['A','B','C','D','E']


# In[43]:


m2= Series(M, index= countries)


# In[44]:


m2


# In[45]:


pd.isnull(m2)


# In[46]:


pd.notnull(m2)


# In[47]:


M_Series


# In[48]:


m2


# In[49]:


M_Series + m2


# In[50]:


m2.index.name= 'Countries'


# In[51]:


m2


# In[65]:


pd.read_xlsx('Pandas.xlsx')


# In[66]:


Data ={'city':['Oman','USA','UAE','UK'], 'Population': [90,300,200,700]}


# In[67]:


Data


# In[68]:


city_frame= DataFrame(Data)


# In[69]:


city_frame


# In[70]:


df= DataFrame(np,array([[1,2,3],[4,5,6],[7,8,9]]), columns=['A','B','C'], index= ['a','b','c'])


# In[75]:


import numpy as np


# In[79]:


df= DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['A','B','C'], index= ['a','b','c'])


# In[80]:


df = DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
columns=['a', 'b', 'c'],index=['A','B','C'])


# In[78]:


df


# In[81]:


df= DataFrame(np.array([[1,2,3],[4,5,6],[7,8,9]]), columns=['A','B','C'], index= ['a','b','c'])


# In[82]:


df


# In[84]:


df= pd.read_xlsx('Pandas..xlsx')


# In[85]:


import pandas as pd


# In[99]:


df = pd.read_csv('Pandas.csv',delimiter=None)


# In[97]:


df


# In[102]:


# Q3:Extract the 'Age' and 'Occupation' columns into a new DataFrame
new_df = df['Age', 'Occupation']


# In[94]:


df.columns


# In[103]:


import numpy as np
from pandas import Series, DataFrame
import pandas as pd
from numpy.random import randn


# In[104]:


#create a new series:
ser1 = Series([1,2,3], index=['A','B','C'])


# In[105]:


ser1


# In[106]:


#Get the index:
ser1.index


# In[107]:


ser1


# In[108]:


ser1.values


# In[109]:


ser2= ser1.reindex(['A','B','C','D','E'])


# In[110]:


ser2


# In[114]:


#fill in values for new indexes:
ser2 = ser1.reindex(['A','B','C','D','E'],fill_value=0)
ser2


# In[118]:


#Using a particular method for filling values:
ser3 = Series(['Oman','USA','UAE'], index=[0,5,10])
ser3

ser3.reindex(range(15), method='ffill')
# In[120]:


ser2 = ser1.reindex(['A','B','C','D','E'],fill_value=0)
ser2


# In[129]:


ser2 = ser1.reindex(['A','B','C','D','E'],fill_value=0)
ser2


# In[130]:


ser3.reindex(range(15), method='bfill')


# In[125]:


ser2 = ser1.reindex(['A','B','C','D','E'], method='0')
ser2


# In[124]:


ser4 = Series([1,2,3,4],index=[0,5,10,14])
ser4


# In[126]:


ser4.reindex(range(15), method='bfill')


# In[127]:


ser4.reindex(range(15), method='ffill')


# In[ ]:




