'''
Exemplo de código para criar um gráfico de linha com seaborn
fonte: https://seaborn.pydata.org/examples/faceted_lineplot.html
'''

# line plots in multiple facets

## Importando packeges
import matplotlib.pyplot as plt
import seaborn as sns 
sns.set_theme(style="ticks")

## Obtendo base de dados - dots 
dots = sns.load_dataset("dots")
#print(dots.sample(3).T)
#print(dots.columns)
# Index(['align', 'choice', 'time', 'coherence', 'firing_rate'], dtype='object')


## Definindo a paleta de cores

palette = sns.color_palette("rocket_r")
## Plotando um grafico de linhas com duas fazer (1 x 2)
ax =sns.relplot(
    kind='line',
    data=dots,
    x='time',
    y='firing_rate',
    hue="coherence",
    size="choice",
    col="align",
    size_order=["T1", "T2"],
    palette=palette,
    height=5,
    aspect=.75,
    facet_kws=dict(sharex=False)
)
ax.fig.suptitle('Gráfico de Linhas')
ax.set_xlabels(label="Time", clear_inner=True)
ax.set_ylabels(label='Firing Rate', clear_inner=True)

#salvando Gráfico
plt.savefig(r"../seaborn/images/lineplot.png")