#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Importing necessary libraries
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


# In[17]:


#Load dataset
iris = pd.read_csv(r'C:\0-College\Projects\iris\iris3.csv')
iris.head()


# In[18]:


iris.describe()


# In[19]:


#View Data Types
iris.dtypes


# In[20]:


# Split into features and target
X = iris.drop(columns=['species'])  
y = iris['species']  

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[21]:


# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)



# In[22]:


# Evaluate model
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")



# In[23]:


# Save model
joblib.dump(model, 'model.pkl')


# In[ ]:




