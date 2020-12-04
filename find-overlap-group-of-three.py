import pandas as pd
from itertools import combinations 
import csv

df = pd.read_csv(r'.\input\guide-loc.txt', sep='\t')
seq= df["Nucleotide sequence"]
start= df["Start"]
end= df["End"]

len= seq.size

comb = combinations(range(0, len), 3)

seqtogether=[]
for i in list(comb):  
    start1 = df.iloc[i[0]][1]
    end1 = df.iloc[i[0]][2]
    
    start2 = df.iloc[i[1]][1]
    end2 = df.iloc[i[1]][2]

    start3 = df.iloc[i[2]][1]
    end3 = df.iloc[i[2]][2]
    
    seqtogether.append ([i, df.iloc[i[0]][0],df.iloc[i[1]][0], df.iloc[i[2]][0], start2-end1, start3-end2])

# rankedlist=sorted(seqtogether,key=lambda x: x[3], reverse= True)
rankedlist=sorted(seqtogether,key=lambda x: (x[4] if x[4] == 0 else -1 / x[4], x[5] if x[5] == 0 else -1 / x[5]  ))


df= pd.DataFrame(rankedlist, columns=["index","guide1","guide2","guide3", 'score', 'score'])
df.to_csv(r'.\output\ranked_guides.txt', sep='\t')