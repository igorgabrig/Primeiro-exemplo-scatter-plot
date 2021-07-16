#Importando as bibliotecas necessárias
import pandas as pd;
import numpy as np;
import seaborn as sns; sns.set();
import matplotlib.pyplot as plt;
import plotly.express as px;
import xlrd;


print("hello");

##Importando o data set
url= ('https://github.com/igorgabrig/Primeiro-exemplo-scatter-plot/blob/main/arq/euro2020.csv?raw=true')
df= pd.read_excel(url)
df.head()

df_sample = df.sample(n=1000)
fig  = px.scatter(df_sample, x = 'Goals', hover_name = "Player", opacity=0.5 ,y = 'Total attempts', log_x = True, width = 800)
fig.update_traces(marker = dict(size = 12, line=dict(width = 2)), selector = dict(mode = 'markers'))
fig.update_layout(title = 'Logaritmo do PIB per capita X Expectativa de vida')
fig.update_xaxes(title = 'Log(PIB per capita)')
fig.update_yaxes(title = 'Expectativa de vida')
fig.show()