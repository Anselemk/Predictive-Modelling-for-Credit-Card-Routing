#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

dataset=pd.read_excel('PSP_Jan_Feb_2019.xlsx')
dataset.head()


# In[12]:


dataset.tail()


# In[14]:


dataset.groupby(['success','PSP'])['amount'].sum()


# In[ ]:




