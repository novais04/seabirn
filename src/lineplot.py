# Gráfoco de linha usando lineplot
# seaborn components used: set_theme(), load_dataset(), lineplot()

# Bibliotecas
import matplotlib.pylab as plt
import seaborn as sns 
sns.set_theme(style='darkgrid')

# # load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
#print(fmri.sample(3))

# plotando o gráfico por diferentes events e regions 
sns.lineplot(
    data=fmri,
    x='timepoint',
    y='signal',
    hue='region',
    style='event'
)

# salvando grafico
plt.savefig(r'../seaborn/reports/lineplot.png')
