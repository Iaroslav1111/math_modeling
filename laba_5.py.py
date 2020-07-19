#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


x=[1,5,5,1,1]


# In[3]:


y=[1,1,5,5,1]


# In[4]:


plt.plot(x,y,color='r',marker='.',ms=10)
plt.xlabel('x')
plt.ylabel('y')
plt.title('laba 1')
plt.grid()

