# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
# import seaborn
import seaborn as sns



df = pd.read_csv(r'.\input\box.txt', sep='\t')
print(df.head(0))

# I1 = df[df['Sample']=='I1']
# I1.shape

# I2 = df[df['Sample']=='I2']
# I2.shape


bp= sns.boxplot(x = 'Sample', y = "%GFP cells", data = df, width=0.8, palette="colorblind", hue= "Day")
bp= sns.stripplot(x='Sample', y= '%GFP cells' , data=df, jitter=True, dodge=True, marker='o', alpha=0.75, color='black', hue="Day")
# bp.get_legend().remove()
# # get legend information from the plot object
labels = bp.get_legend_handles_labels()
handles= bp.get_legend_handles_labels()
print(labels)
print(handles)
# # specify just one legend
l = plt.legend(handles, labels)


plt.show()

# sns.boxplot(x = "Day", y = "%GFP cells", data = I2, width=0.5, palette="colorblind")
# sns.stripplot(x='Day', y= '%GFP cells' , data=I2, jitter=True, marker='o', alpha=0.75, color='black')
# plt.show()

# # make boxplot with Seaborn
# bplot=sns.boxplot(y='Day 13', x='Sample', 
#                  data=dataset, 
#                  width=0.5,
#                  palette="colorblind")
 
# # add stripplot to boxplot with Seaborn
# bplot=sns.stripplot('Day 13', x='Sample', 
#                    data=dataset, 
#                    jitter=True, 
#                    marker='o', 
#                    alpha=0.5,
#                    color='black')

# plt.show