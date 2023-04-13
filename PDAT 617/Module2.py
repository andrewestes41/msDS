#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1) Write a NumPy program to create an empty and a full array.(10 points)
import numpy as np

empty = np.empty((3, 4), dtype=int)
empty


# In[4]:


full = np.full((4,3), 12, dtype=int)
full


# In[10]:


# 2) Write a NumPy program to get the unique elements of an array.
original = np.array(['a', 'b', 'b', 'b', 2, 2, 3, 4, 1, 1, 1, 1, 1])
original


# In[11]:


np.unique(original)


# In[46]:


# 3) Write a NumPy program to construct an array by repeating
x = np.array([[1, 2, 3]])
np.repeat(x, 2)


# In[47]:


np.tile(x, 2)


# In[48]:


# 4) Write a NumPy program to sort pairs of first name and last name return their indices.
first_names = ("Betsey", "Shelley", "Lanell", "Genesis", "Margery")
last_names = ("Battle", "Brien", "Plotner", "Stahl", "Woolum")

z = np.lexsort((last_names, first_names))
z


# In[49]:


# 5) Write a Python program to count number of occurrences of each value in a given array of non-negative integers.
given = np.array([0, 1, 6, 1, 4, 1, 2, 2, 7])

np.array(np.unique(given, return_counts=True)).T


# In[56]:


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter= ',' , dtype = 'object')
sepallength = np.genfromtxt(url, delimiter= ',', dtype = 'float', usecols =[0])


# In[61]:


# 1) Find the mean, median, standard deviation of iris’s sepallength (1st column)
np.mean(sepallength)


# In[62]:


np.median(sepallength)


# In[64]:


np.std(sepallength)


# In[66]:


# 2) Find the 5th and 95th percentile of iris’s sepallength.
q95, q5 = np.percentile(x, [95, 5])
q95


# In[67]:


q5


# In[75]:


# 3) Create a normalized form of iris’s sepallength whose values range exactly between 0 and 1 
#so that the minimum has value 0 and maximum has value 1
Smax, Smin = sepallength.max(), sepallength.min()
S = (sepallength - Smin)/(Smax - Smin)

S


# In[76]:


# 4) Filter the rows of iris that has petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0.
#https://pythontraining.dzone.co.in/tutorial/exercises/numpy/numpy-exercise_3.html
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

condition = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
iris_2d[condition]


# In[ ]:




