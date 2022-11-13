# -*- coding: utf-8 -*-
"""lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RsKqNxGsw9grhage_l0NFU-n2KlGsFui
"""

import seaborn as sns
penguins = sns.load_dataset('penguins')
penguins
penguins = penguins.dropna()
penguins

from sklearn import preprocessing
le = preprocessing.LabelEncoder()
for column_name in penguins.columns:
  if penguins[column_name].dtype == object:
    penguins[column_name] = le.fit_transform(penguins[column_name])
  else:
    pass

penguins

from sklearn.model_selection import train_test_split

X_penguins = penguins.drop('species', axis=1)

y_penguins = penguins['species']

Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

from sklearn.naive_bayes import GaussianNB # 1. Выбираем класс модели
model = GaussianNB()                       # 2. Инициализируем модель
model.fit(Xtrain, ytrain)                  # 3. Обучаем модель
y_model = model.predict(Xtest)             # 4. Выполняем классификацию

from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

X_penguins = penguins.drop(['species','island'], axis=1)

y_penguins = penguins['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

model = GaussianNB()                       
model.fit(Xtrain, ytrain)                 
y_model = model.predict(Xtest)    

accuracy_score(ytest, y_model)

X_penguins = penguins.drop(['species','island','bill_length_mm'], axis=1)

y_penguins = penguins['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

model = GaussianNB()                       
model.fit(Xtrain, ytrain)                 
y_model = model.predict(Xtest)    

accuracy_score(ytest, y_model)

X_penguins = penguins.drop(['species','island','bill_length_mm','bill_depth_mm'], axis=1)

y_penguins = penguins['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

model = GaussianNB()                       
model.fit(Xtrain, ytrain)                 
y_model = model.predict(Xtest)    

accuracy_score(ytest, y_model)

X_penguins = penguins.drop(['species','island','bill_length_mm','bill_depth_mm','flipper_length_mm'], axis=1)

y_penguins = penguins['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

model = GaussianNB()                       
model.fit(Xtrain, ytrain)                 
y_model = model.predict(Xtest)    

accuracy_score(ytest, y_model)

X_penguins = penguins.drop(['species','island','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g'], axis=1)

y_penguins = penguins['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

model = GaussianNB()                       
model.fit(Xtrain, ytrain)                 
y_model = model.predict(Xtest)    

accuracy_score(ytest, y_model)

X_penguins = penguins.drop(['species','bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g','sex'], axis=1)

y_penguins = penguins['species']
Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

model = GaussianNB()                       
model.fit(Xtrain, ytrain)                 
y_model = model.predict(Xtest)    

accuracy_score(ytest, y_model)

penguins.columns.tolist()

from sklearn.metrics import confusion_matrix
col = penguins.columns.tolist()
col.pop()
m = []
for i in col:
  m.append(i)
  
  X_penguins = penguins.drop(m, axis=1)

  y_penguins = penguins['species']
  Xtrain, Xtest, ytrain, ytest = train_test_split(X_penguins, y_penguins,test_size=0.15,random_state=1)

  model = GaussianNB()                       
  model.fit(Xtrain, ytrain)                 
  y_model = model.predict(Xtest)   

  print("Исключение признаков: ") 
  print(m)

  #print(y_model)
  
  print("Точность прогноза: ")
  print(accuracy_score(ytest, y_model))
  print("Матрица несоответствий: ")
  print(confusion_matrix(ytest, y_model))
  print("__________________________________________________________________")

from sklearn.metrics import confusion_matrix
target_names=[]
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
confusion_matrix(y_true, y_pred)