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

df.columns = ['start' if x ==
              'Start' else x for x in df.columns]
start = df['start']

df.columns = ['end' if x ==
              'End' else x for x in df.columns]
end = df['end']

# remove NGG from the ecrisp sequence and remove three nucleotides from the end
ecrisp= df['ecrisp'].str.replace(r' NGG$', '')
end= end.sub(3)

# Combine all dataframes into four columns and write to csv file
combined = pd.concat([crispick, ecrisp, start, end], join = 'outer', axis = 1) 
combined.to_csv(r'./output/compare_guides.txt', sep='\t', index = False)

# Read in txt file that contains crispick and ecrisp guides
df = pd.read_csv(r'.\output\compare_guides.txt', sep='\t')

# finds the instersection of the crispick and ecrisp sgRNAs and preserves the genome locations associated with the ecrisp list
intersection = df.merge(df, how = 'inner', left_on = ['crispick'], right_on=['ecrisp'])
intersection.drop(columns=['crispick_x', 'crispick_y','ecrisp_x','start_x','end_x'], inplace = True)
intersection.rename(columns={'ecrisp_y': 'Nucleotide sequence', 'start_y': 'Start', 'end_y': 'End'}, inplace = True)

# write the common sgRNAs and the start and end locations out to a new text file
intersection.to_csv(r'.\output\common_sgrnas.txt', sep='\t', index=False)