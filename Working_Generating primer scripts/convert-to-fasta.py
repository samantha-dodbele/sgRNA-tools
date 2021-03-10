
import pandas as pd

# Read in xlsx file named 'guides' on desktop
df = pd.read_excel(r'.\input\guides.xlsx')

length = len(df["Guides"])
fasta = []
for x in range(0, length):
    fasta.append("> seq"+str(x+1))
    fasta.append(str(df["Guides"][x]))

with open('./output/fasta.txt','w') as f:
    f.write('\n'.join(fasta))
