import numpy as np
import matplotlib.pyplot as plt
print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
import pandas as pd
dataset = pd.read_csv("iris.csv")
x = dataset.iloc[:,:-1].values
y = dataset['variety'].values
dataset.head(5)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(y_pred)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
from sklearn.metrics import accuracy_score
print("Accuracy : ",accuracy_score(y_test, y_pred))
df = pd.DataFrame({'Real values':y_test,'Predicted values':y_pred})
print(df)