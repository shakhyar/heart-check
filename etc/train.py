#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np

cl = pd.read_csv("data/processed.hungarian.data")
hn = pd.read_csv("data/processed.hungarian.data")
sw = pd.read_csv("data/processed.switzerland.data")
va = pd.read_csv("data/processed.va.data")


# In[6]:


classes = ['age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
           'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

classes_to_drop = ['exang', 'oldpeak', 'slope', 'ca', 'thal']

cl.columns = classes
hn.columns = classes
sw.columns = classes
va.columns = classes

for i in classes_to_drop:
    cl.drop(i, inplace=True, axis=1)
    hn.drop(i, inplace=True, axis=1)
    sw.drop(i, inplace=True, axis=1)
    va.drop(i, inplace=True, axis=1)


# In[7]:


age = []
gender = [] 
cp = []
trestbps =[] 
chol = []
fbs = []
restecg =[]
thalach = []
target =[] 


# In[8]:


age = [cl['age'].tolist(), hn['age'].tolist(), sw['age'].tolist(), va['age'].tolist()]
gender = [cl['gender'].tolist(), hn['gender'].tolist(), sw['gender'].tolist(), va['gender'].tolist()]
cp = [cl['cp'].tolist(), hn['cp'].tolist(), sw['cp'].tolist(), va['cp'].tolist()]
trestbps = [cl['trestbps'].tolist(), hn['trestbps'].tolist(), sw['trestbps'].tolist(), va['trestbps'].tolist()]
chol = [cl['chol'].tolist(), hn['chol'].tolist(), sw['chol'].tolist(), va['chol'].tolist()]
fbs = [cl['fbs'].tolist(), hn['fbs'].tolist(), sw['fbs'].tolist(), va['fbs'].tolist()]
restecg = [cl['restecg'].tolist(), hn['restecg'].tolist(), sw['restecg'].tolist(), va['restecg'].tolist()]
thalach = [cl['thalach'].tolist(), hn['thalach'].tolist(), sw['thalach'].tolist(), va['thalach'].tolist()]
target = [cl['target'].tolist(), hn['target'].tolist(), sw['target'].tolist(), va['target'].tolist()]


# In[9]:


data = pd.DataFrame({"age": age[0]+age[1]+age[2],
                    "gender": gender[0]+gender[1]+gender[2], 
                    "cp": cp[0]+cp[1]+cp[2],
                     "trestbps": trestbps[0]+trestbps[1]+trestbps[2],
                     'chol': chol[0]+chol[1]+chol[2],
                     'fbs': fbs[0]+fbs[1]+fbs[2],
                     'restecg': restecg[0]+restecg[1]+restecg[2],
                     'thalach': thalach[0]+thalach[1]+thalach[2],
                     'target': target[0]+target[1]+target[2]
                     })
data = data.replace(to_replace ="?",
                 value =-1)


# In[11]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pickle


# In[20]:


x = data.drop(['target'], axis = 1)
y = data['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 0)


# In[21]:


k = 1
knn_classifier = KNeighborsClassifier(n_neighbors = k)
knn_classifier.fit(x_train, y_train)
score = 0
score = knn_classifier.score(x_test, y_test)
print(score)


# In[23]:


# testing

model = knn_classifier

pred = np.array([73,0,3,160,0,0,1,121]) # ground truth = 1
p = pred.reshape(-1, 1)
p = p.reshape(1, 8)


history = model.predict(p)
print(history)


# In[40]:


#save the model
pickle.dump(model, open('saved/model', 'wb'))