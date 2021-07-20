#Importando as bibliotecas necessárias
import pandas as pd;
import numpy as np;
import seaborn as sns; sns.set();
import matplotlib.pyplot as plt;
import plotly.express as px;
import xlrd;
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

print("hello");

##Importando o data set
url= ('https://github.com/igorgabrig/Primeiro-exemplo-scatter-plot/blob/main/arq/db.xlsx?raw=true')
df= pd.read_excel(url)
df.head()

df.info()

#sns.pairplot(df, height=3.0)
#plt.show()


#df.boxplot(column='Rate')
#plt.show()

#df.boxplot(column='Metascore')
#plt.show()

#df.boxplot(column='Budget')
#plt.show()

#df.boxplot(column='Opening Weekend USA')
#plt.show()

#df.boxplot(column='Gross USA')
#plt.show()

#df.boxplot(column='Gross Worldwide')
#plt.show()



#plt.figure(figsize=(7,7))
#plt.pie(x=df['Rate'], labels=df['Original Title'], autopct='%1.1f%%', startangle=90)

#plt.show()

iris = load_iris()

X = df.drop(['Rate','Metascore'], axis = 1).values
y = df.values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.30, random_state=13)

n_neighbors = 10

clf = KNeighborsClassifier(n_neighbors=n_neighbors)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred, target_names=iris.target_names))