import matplotlib.pyplot as plt
import seaborn as sns 
sns.set_theme(style='whitegrid')

# obeter dados
penguins = sns.load_dataset("penguins")

# desnhando o barplot de especies e sex
ax = sns.catplot(
    kind='bar',
    data=penguins,
    x="species",
    y="body_mass_g",
    hue='sex',
    errorbar="sd",
    palette="dark",
    alpha=.6,
    height=6
)

ax.set_xlabels("Espécies", fontsize=14)
ax.set_ylabels("Massa Corporal (g)", fontsize=14)
ax.legend.set_title("Legenda")
#sns.move_legend(ax,'upper right')

plt.title("Grouped Barplot")
# save fig 
plt.savefig(r'../seaborn/reports/barplot.png')