# Fonte: https://sigmoidal.ai/como-fazer-graficos-rotulados-em-python/

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set_theme(style='ticks')

#criando o DataFrame
df = pd.DataFrame({'Frutas':['Laranja','Maçã','Melão','Kiwi','Banana'], # Nome das frutas
                   'Quantidade':[200,500,1200,600,800]})  # Quantidade vendida de cada fruta
#ajustando a ordem do DataFrame
df.sort_values(by='Quantidade', # ordenar pela quantidade
               ascending=False, # colocar na ordem contrária a ascendente (portanto, descendente <- maior para o menor)
               inplace=True, # atualizar o DataFrame com as mudanças
               ignore_index=True) #ignorar índice anterior
#print(df.sample(4))

# criando a figura
fig, ax = plt.subplots(figsize=(8,6))

# plotando o Gráfico
sns.barplot(data=df, x='Frutas', y='Quantidade')

plt.title("Gráfico de Barras com Rótulos")










# salvando a figura
plt.savefig(r'../seaborn/reports/barplot_rotulos.png')