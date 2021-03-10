import pandas as pd

# Read in CRISPick output file, pick out sgRNA sequences, and write the sgRNAs out to a new csv file
df = pd.read_csv(r'.\input\sgrna-designs.txt', sep='\t')
df.columns = ['crispick' if x == 'sgRNA Sequence' else x for x in df.columns]
crispick = df['crispick']

# Read in Ecrisp output file, pick out sgRNA sequences, strip NGG and write the sgRNAs out to a new csv file
df = pd.read_csv(r'.\input\all_results_together.tab', sep='\t')
df.columns = ['ecrisp' if x ==
              'Nucleotide sequence' else x for x in df.columns]
ecrisp = df['ecrisp']

ecrisp= df['ecrisp'].str.replace(r' NGG$', '')

# Combine both dataframes into two columns and write to csv file
combined = pd.concat([crispick, ecrisp], join = 'outer', axis = 1) 
combined.to_csv(r'./output/compare_guides.txt', sep='\t', index = False)

# Read in txt file that contains crispick and ecrisp guides
df = pd.read_csv(r'.\output\compare_guides.txt', sep='\t')

list1 = df['crispick'].tolist()
list2 = df['ecrisp'].tolist()

s_list1 = set(list1)
s_list2 = set(list2)

# sgRNAs in common between all three lists
intersection_1 = s_list1.intersection(s_list2)
intersection_as_list = list(intersection_1)

# common in between 1 and 2
print("Common in between 1 and 2: "+str(len(intersection_1)))

with open('./output/common_sgrnas.txt', 'w') as f:
    f.write('\n'.join(intersection_as_list))

# Read in csv file containing common guides 
df = pd.read_csv(r'.\output\common_sgrnas.txt', sep='\t', header= None)

length = df.size
fasta = []
for x in range(0, length):
     fasta.append("> seq"+str(x+1))
     fasta.append(str(df.iloc[x, 0]))

with open('./output/fasta.txt','w') as f:
      f.write('\n'.join(fasta))

