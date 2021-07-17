#Importando as bibliotecas necessárias
import pandas as pd;
import numpy as np;
import seaborn as sns; sns.set();
import matplotlib.pyplot as plt;
import plotly.express as px;
import xlrd;



print("hello");

##Importando o data set
url= ('https://github.com/igorgabrig/Primeiro-exemplo-scatter-plot/blob/main/arq/db.xlsx?raw=true')
df= pd.read_excel(url)
df.head()

print(df['Budget'])

#sns.pairplot(df, height=3.0)
#plt.show()


df.boxplot(column='Rate')
plt.show()

df.boxplot(column='Metascore')

#df.boxplot(column='Budget')
plt.show()