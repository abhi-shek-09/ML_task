#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


m=np.linspace(0,10,11)
print(f"The array m should look like this: \n{m}")


# In[4]:


c=3 * (10**8)
e=m*c**2
print(f"The array E should look like this: \n{e}")


# In[8]:


plt.plot(m,e,color='red',lw=4)
plt.title("e=mc^2")
plt.xlabel("Mass in grams")
plt.ylabel("Energy in Joules")
plt.xlim(0,10)
plt.show()


# In[9]:


plt.plot(m,e,color='red',lw=4)
plt.title("e=mc^2")
plt.xlabel("Mass in grams")
plt.ylabel("Energy in Joules")
plt.xlim(0,10)
plt.yscale("log")
plt.grid(which='both',axis='y')
plt.show()


# In[10]:


labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]


# In[11]:


f = plt.figure()
axes = f.add_axes([0,0,1,1])
axes.plot(labels, july16_2007,label='july16_2007')
axes.plot(labels,july16_2020,label='july16_2020')
plt.legend()
plt.show()


# In[15]:


f = plt.figure()
axes = f.add_axes([0,0,1,1])
axes.plot(labels, july16_2007,label='july16_2007')
axes.plot(labels,july16_2020,label='july16_2020')
plt.legend(loc=(1,0))
plt.show()


# In[16]:


f,axes = plt.subplots(nrows=2,ncols=1,figsize=(10,10))
axes[0].plot(labels, july16_2007,label='july16_2007')
axes[0].set_title("July 16th, 2007")
axes[1].plot(labels,july16_2020,label='july16_2020')
axes[1].set_title("July 16th, 2020")
plt.show()


# In[ ]:


#will figure out bonus task asap

