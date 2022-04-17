#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


np.zeros(10)


# In[3]:


np.ones(10)


# In[5]:


np.ones(10)*5


# In[6]:


np.arange(10,51)


# In[7]:


np.arange(10,51,2)


# In[8]:


np.arange(0,9).reshape(3,3)


# In[9]:


np.eye(3)


# In[10]:


np.random.rand(1)


# In[11]:


ranarr = np.random.rand(25)


# In[12]:


ranarr


# In[14]:


np.arange(0.01,1.01,0.01).reshape(10,10)


# In[17]:


np.linspace(0,1,20)


# In[18]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[19]:


mat[2:,1:]


# In[25]:


mat[0:3,1:2]


# In[26]:


mat[4]


# In[27]:


mat[3:]


# In[28]:


mat.sum()


# In[29]:


mat.std()


# In[30]:


mat.sum(axis=0)


# In[ ]:


#seed in random module

