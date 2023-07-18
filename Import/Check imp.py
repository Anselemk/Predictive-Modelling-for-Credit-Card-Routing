#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np

dataset=pd.read_excel('PSP_Jan_Feb_2019.xlsx')
dataset.head()


# In[8]:


dataset.groupby(['PSP'])['amount'].sum()


# In[ ]:




