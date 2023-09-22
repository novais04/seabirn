# import pachegers
import matplotlib.pyplot as plt
import seaborn as sns 

# Loadind dataset
data = sns.load_dataset('iris')
#data.to_csv(r"../seaborn/data/iris.csv")

#print(data.columns)
# draw lineplot
sns.lineplot(
    data=data,
    x='sepal_length', 
    y='sepal_width',
)
#plt.savefig(r"../seaborn/images/line_plot_v01.png")
plt.show()
