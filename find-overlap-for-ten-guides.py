import pandas as pd
from itertools import combinations 
import csv

df = pd.read_csv(r'.\input\guide-loc.txt', sep='\t')
seq= df["Nucleotide sequence"]
start= df["Start"]
end= df["End"]

len= seq.size

comb = combinations(range(0, len), 10)

seqtogether=[]
for i in list(comb):  
    start1 = df.iloc[i[0]][1]
    end1 = df.iloc[i[0]][2]
    
    start2 = df.iloc[i[1]][1]
    end2 = df.iloc[i[1]][2]

    start3 = df.iloc[i[2]][1]
    end3 = df.iloc[i[2]][2]

    start4 = df.iloc[i[3]][1]
    end4 = df.iloc[i[3]][2]

    start5 = df.iloc[i[4]][1]
    end5 = df.iloc[i[4]][2]

    start6 = df.iloc[i[5]][1]
    end6 = df.iloc[i[5]][2]

    start7 = df.iloc[i[6]][1]
    end7 = df.iloc[i[6]][2]

    start8 = df.iloc[i[7]][1]
    end8 = df.iloc[i[7]][2]

    start9 = df.iloc[i[8]][1]
    end9 = df.iloc[i[8]][2]

    start10 = df.iloc[i[9]][1]
    end10 = df.iloc[i[9]][2]
    
    seqtogether.append ([i, start2-end1, start3-end2, start4-end3, start5-end4, start6-end5, start7-end6, start8-end9, start9-end10, start10-end1])

    # seqtogether.append ([i, df.iloc[i[0]][0],df.iloc[i[1]][0], df.iloc[i[2]][0], start2-end1, start3-end2])

# rankedlist=sorted(seqtogether,key=lambda x: x[3], reverse= True)
rankedlist=sorted(seqtogether,key=lambda x: x[2], reverse= True)


df= pd.DataFrame(rankedlist, columns=["index", 'score', 'score', 'score', 'score', 'score', 'score', 'score', 'score', 'score'])
df.to_csv(r'.\output\ranked_guides.txt', sep='\t')