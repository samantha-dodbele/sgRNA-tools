import pandas as pd
from itertools import combinations 
import csv

df = pd.read_csv(r'.\input\guide-loc.txt', sep='\t')
seq= df["Nucleotide sequence"]
start= df["Start"]
end= df["End"]

len= seq.size

comb = combinations(range(0, len), 2)

seqtogether=[]
for i in list(comb):  
    start1 = df.iloc[i[0]][1]
    end1 = df.iloc[i[0]][2]
    
    start2 = df.iloc[i[1]][1]
    end2 = df.iloc[i[1]][2]
    
    seqtogether.append ([i, df.iloc[i[0]][0],df.iloc[i[1]][0], start2-end1])

rankedlist=sorted(seqtogether,key=lambda x: x[3], reverse=True)

df= pd.DataFrame(rankedlist, columns=["index","guide1","guide2", 'score'])
df.to_csv(r'.\output\ranked_guides.txt', sep='\t')