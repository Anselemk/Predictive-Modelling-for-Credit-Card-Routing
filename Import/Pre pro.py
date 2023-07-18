#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pandas as pd
import numpy as np


raw_dataset=pd.read_excel('PSP_Jan_Feb_2019.xlsx')
raw_dataset=pd.DataFrame(raw_dataset)
raw_dataset.tail()


# In[29]:


raw_dataset.card.unique()


# In[37]:





# In[36]:


print(raw_dataset.loc[0,'country'])


# In[38]:


prepros_dataset=pd.DataFrame()
for i in range(len(raw_dataset)):
    if  raw_dataset.iloc[i,2]=='Germany':
        prepros_dataset.loc[i,'Is_Germany']=1
        prepros_dataset.loc[i,'Is_Austria']=0
        prepros_dataset.loc[i,'Is_Switzerland']=0
    elif raw_dataset.iloc[i,2]=='Austria':
        prepros_dataset.loc[i,'Is_Germany']=0
        prepros_dataset.loc[i,'Is_Austria']=1
        prepros_dataset.loc[i,'Is_Switzerland']=0
    elif raw_dataset.iloc[i,2]=='Switzerland':
        prepros_dataset.loc[i,'Is_Germany']=0
        prepros_dataset.loc[i,'Is_Austria']=0
        prepros_dataset.loc[i,'Is_Switzerland']=1

prepros_dataset.head()


# In[39]:


prepros_dataset.tail()


# In[ ]:




