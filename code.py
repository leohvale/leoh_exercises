# comandos git para adicionar e commitar os arquivos

import pandas as pd

gasolina_df = pd.read_csv('gasolina.csv')

import seaborn as sns

plot = sns.lineplot(x='dia', y='venda', data=gasolina_df)


fig = plot.get_figure()
fig.savefig("grafico.png") 
