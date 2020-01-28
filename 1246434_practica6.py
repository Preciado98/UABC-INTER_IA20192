#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.model_selection import GridSearchCV
import numpy as np

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7)

desicion = tree.DecisionTreeClassifier()
param = {'criterion':['gini','entropy'],
              'splitter':['best','random'],
              'max_depth':np.linspace(2,10,9),
              'min_samples_split':np.linspace(000.1,1,100)}

clf = GridSearchCV(desicion, param,cv=4)
clf.fit(X_train,  y_train)

#reg_log = LogisticRegression(solver='lbfgs', multi_class='auto')
#reg_log.fit(X_train, y_train)
#y_pred = reg_log.predict(X_test)

#cnf_matrix = confusion_matrix(y_test, y_pred)
#print(cnf_matrix)

#print('Acc: ',accuracy_score(y_test, y_pred))
#print('P: ',precision_score(y_test, y_pred, average='macro'))
#print('R: ',recall_score(y_test, y_pred, average='macro'))
#print('F1: ',f1_score(y_test, y_pred, average='macro'))


# In[8]:


clf.best_score_


# In[9]:


clf.best_params_


# In[ ]:




