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
combined.to_csv(r'./output/compareguides.txt', sep='\t', index = False)