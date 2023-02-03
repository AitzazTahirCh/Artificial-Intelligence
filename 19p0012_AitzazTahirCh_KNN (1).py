#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
from collections import Counter


# In[16]:


df = pd.read_csv("fruit_data_with_colors.txt",delimiter = "\t")


# In[17]:


df


# In[18]:


X = df[["mass","width","height"]]


# In[19]:


Y = df["fruit_label"]


# In[20]:


trainX = np.array(X[:50])
trainY = np.array(Y[:50])
testX = np.array(X[50:])
testY = np.array(Y[50:])


# In[21]:


class KNN:
    def __init__(self,k = 1):
        self.k = k
        
    def euclidian_distance(self,query,X):
        difference = np.array(X) - np.array(query)
        sqrd_diff = np.square(difference)
        sum_sqrd_diff = np.sum(sqrd_diff, axis = 1)
        distance = np.sqrt(sum_sqrd_diff)
        return distance
    
    def nearest_neighbours(self,distance):
        return np.argsort(distance)[:self.k]
    
    def predict(self,query,trainX,trainY):
        ed = self.euclidian_distance(query,trainX)
        nn = self.nearest_neighbours(ed)
        labels_nn = list(trainY[nn])
        return max(labels_nn, key = labels_nn.count) 
    


# In[22]:


classifier = KNN(1)


# In[31]:


dist=[classifier.euclidian_distance(x,trainX) for x in testX]
dist


# In[32]:


predictions = [classifier.predict(x,trainX,trainY) for x in testX]


# In[33]:


predictions


# In[34]:


testY


# In[35]:


from sklearn.metrics import accuracy_score
a = accuracy_score(testY, predictions)
a


# In[13]:


from sklearn.metrics import confusion_matrix
b = confusion_matrix(testY, predictions)
b

