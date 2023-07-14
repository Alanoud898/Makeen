#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas library
import pandas as pd
 
# Create empty dataframe
df = pd.DataFrame()
 
# Creating a simple dataframe
df['name'] = ['Maathar', 'Jihan', 'Maya',
              'Fatema', 'Asma', 'Alanoud']
df['major'] = ['IT', 'IT', 'CS', 'CS', 'Stat', 'IT']
df['age'] = [23, 40, 19, 26, 28, 33]
 
# View dataframe
df


# In[2]:


# function to find mean
def mean_age_by_group(dataframe, col):
   
    # groups the data by a column and
    # returns the mean age per group
    return dataframe.groupby(col).mean()
   
# function to convert to uppercase
def uppercase_column_name(dataframe):
   
    # Converts all the column names into uppercase
    dataframe.columns = dataframe.columns.str.upper()
     
    # And returns them
    return dataframe 


# In[3]:


# Create a pipeline that applies both the functions created above
pipeline = df.pipe(mean_age_by_group, col='major').pipe(uppercase_column_name)

# calling pipeline
pipeline


# In[4]:


pip install pdpipe


# In[5]:


# importing the package
import pdpipe as pdp
import pandas as pd

# creating a empty dataframe named dataset
dataset = pd.DataFrame()

# Creating a simple dataframe
dataset['name'] = ['Reema', 'Shyam', 'Jai','Nimisha', 'Rohit', 'Riya']

dataset['gender'] = ['Female', 'Male', 'Male','Female', 'Male', 'Female']

dataset['age'] = [31, 32, 19, 23, 28, 33]

dataset['department'] = ['Accounts', 'Management','IT', 'IT', 'Management','Advertising']

dataset['index'] = [1, 2, 3, 4, 5, 6]

# View dataframe
dataset


# In[6]:


# creating a pipeline and
# dropping the unwanted column
dropCol = pdp.ColDrop("index").apply(dataset)

# display the new dataframe
# after column drop
dropCol


# In[7]:


# creating a pipeline and
# dropping the unwanted column
dropCol2 = pdp.ColDrop("index")

# applying the ColDrop to dataframe
df2 = dropCol2(dataset)

# display dataframe
df2


# In[10]:


# importing the package
import pdpipe as pdp
import pandas as pd

# creating a empty dataframe named dataset
dataset = pd.DataFrame()

# Creating a simple dataframe
dataset['name'] = ['Reema', 'Shyam', 'Jai','Nimisha', 'Rohit', 'Riya']

dataset['gender'] = ['Female', 'Male', 'Male','Female', 'Male', 'Female']

dataset['age'] = [31, 32, 19, 23, 28, 33]

dataset['department'] = ['Accounts', 'Management','IT', 'IT', 'Management','Advertising']

dataset['index'] = [1, 2, 3, 4, 5, 6]

# View dataframe
dataset


# In[9]:


#dropping the values using ValDrop
df3 = pdp.ValDrop(['IT'],'department').apply(dataset)

#display dataframe
df3


# In[ ]:




