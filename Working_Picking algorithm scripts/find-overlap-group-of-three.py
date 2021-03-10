import pandas as pd
from itertools import combinations 
import csv

df = pd.read_csv(r'.\input\guide-loc.txt', sep='\t')
seq= df["Nucleotide sequence"]
start= df["Start"]
end= df["End"]

result= df.sort_values(by=['Start'])
result.to_csv(r'.\output\sorted_guides.txt', sep='\t', index=False)

len= seq.size
comb = combinations(range(0, len), 3)

seqtogether=[]
for i in list(comb):  
    start1 = result.iloc[i[0]][1]
    end1 = result.iloc[i[0]][2]
    
    start2 = result.iloc[i[1]][1]
    end2 = result.iloc[i[1]][2]

    start3 = result.iloc[i[2]][1]
    end3 = result.iloc[i[2]][2]
    
    seqtogether.append ([i, result.iloc[i[0]][0],result.iloc[i[1]][0], result.iloc[i[2]][0], start2-end1, start3-end2])

# rankedlist=sorted(seqtogether,key=lambda x: x[3], reverse= True)
rankedlist=sorted(seqtogether,key=lambda x: (x[4] if x[4] == 0 else -1 / x[4], x[5] if x[5] == 0 else -1 / x[5]  ))

result= pd.DataFrame(rankedlist, columns=["index","guide1","guide2","guide3", 'score', 'score'])
result.to_csv(r'.\output\ranked_guides.txt', sep='\t', index=False)