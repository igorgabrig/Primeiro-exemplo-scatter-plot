#Importando as bibliotecas necessárias
import pandas as pd;
import numpy as np;
import seaborn as sns; sns.set();
import matplotlib.pyplot as plt;
import plotly.express as px;
import xlrd;



print("hello");

##Importando o data set
url= ('https://github.com/igorgabrig/Primeiro-exemplo-scatter-plot/blob/main/arq/euro2020.xlsx?raw=true')
df= pd.read_excel(url)
df.head()

#print(df)

sns.pairplot(df)

plt.show()