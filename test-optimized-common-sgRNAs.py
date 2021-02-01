import pandas as pd
import csv
import statistics
from xlwt import Workbook
from utils import *

# read in the common sgRNAs and thier genome locations
df = pd.read_csv(r'C:\Users\Samantha\Box Sync\Wilusz Lab\Test\20\output_guide-loc.txt', sep='\t')
seq= df["Nucleotide sequence"]
start= df["Start"]
end= df["End"]

# Sort the guides by genome location and remove duplicates
df.drop_duplicates(inplace=True)
df = df.sort_values(by=['Start'])
df.to_csv(r'C:\Users\Samantha\Box Sync\Wilusz Lab\Test\20\output_sorted_guides.txt', sep='\t', index=False)

# if there are more than 11 guides then go through guides and check if a guide's start is within 3 nt of it if so delete the second instance

dfCopy = df.copy()
dfCopy = dfCopy.sort_values(by=['Start'])
dfCopy = dfCopy.reset_index(drop=True)
dfCopy["id"] = dfCopy.index
dfCopy2 = dfCopy.copy()
dfCopy2["nextId"] = dfCopy2['id'] + 1
dfSelfJoin = pd.merge(dfCopy2, dfCopy, how="inner", left_on='nextId', right_on='id', suffixes=('','_y'))
dfSelfJoin["diff"] = dfSelfJoin["Start_y"] - dfSelfJoin["Start"]
dfSelfJoin = dfSelfJoin[dfSelfJoin["diff"] <= 3]
dfRemove = dfSelfJoin[['Start']]
df = df[~df['Start'].isin(dfRemove['Start'].values)]
df.to_csv(r'C:\Users\Samantha\Box Sync\Wilusz Lab\Test\20\output_dedeup-guides.txt', sep='\t', index=False)

    


