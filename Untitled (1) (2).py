#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

dataset=pd.read_excel('PSP_Jan_Feb_2019.xlsx')
dataset.head()


# In[11]:


dataset.tail()


# In[12]:


dataset.groupby(['success','PSP'])['amount'].sum()


# In[ ]:


set_nb_theme('grade3')


# In[ ]:


from jupyterthemes import get_themes
from jupyterthemes.stylefx import set_nb_theme


# In[ ]:


set_nb_theme('onedork')


# In[13]:


from jupyterthemes import get_themes
from jupyterthemes.stylefx import set_nb_theme


# In[14]:


set_nb_theme('grade3')


# In[ ]:




