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


# In[6]:


set_nb_theme('grade3')


# In[7]:


from jupyterthemes import get_themes
from jupyterthemes.stylefx import set_nb_theme


# In[8]:


set_nb_theme('onedork')


# In[ ]:




