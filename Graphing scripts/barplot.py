# import pandas
import pandas as pd
# import matplotlib
import matplotlib.pyplot as plt
# import seaborn
import seaborn as sns



df = pd.read_csv(r'.\input\bar.txt', sep='\t')
print(df.head(0))

bp= sns.barplot(x = 'Puro', y = "%GFP cells", data = df, hue= "Day", palette="colorblind")
#  width=0.8, palette="colorblind", hue= "Day")
# bp= sns.stripplot(x='Sample', y= '%GFP cells' , data=df, jitter=True, dodge=True, marker='o', alpha=0.75, color='black', hue="Day")
bp.set(xlabel= 'PCNA-1', ylabel='%GFP+ cells Normalized to Day 3')

# handles, labels = bp.get_legend_handles_labels()

# When creating the legend, only use the first four elements to effectively remove the last four.
# l = plt.legend(handles[0:4], labels[0:4])

plt.show()