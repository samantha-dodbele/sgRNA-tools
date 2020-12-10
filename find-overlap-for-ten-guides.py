import pandas as pd
from itertools import combinations 
import csv
import statistics

df = pd.read_csv(r'.\input\guide-loc.txt', sep='\t')
seq= df["Nucleotide sequence"]
start= df["Start"]
end= df["End"]

result= df.sort_values(by=['Start'])
result.to_csv(r'.\output\sorted_guides.txt', sep='\t', index=False)

len= seq.size
comb = combinations(range(0, len), 10)

seqtogether=[]
for i in list(comb):  
    start1 = result.iloc[i[0]][1]
    end1 = result.iloc[i[0]][2]
    
    start2 = result.iloc[i[1]][1]
    end2 = result.iloc[i[1]][2]

    start3 = result.iloc[i[2]][1]
    end3 = result.iloc[i[2]][2]

    start4 = result.iloc[i[3]][1]
    end4 = result.iloc[i[3]][2]

    start5 = result.iloc[i[4]][1]
    end5 = result.iloc[i[4]][2]

    start6 = result.iloc[i[5]][1]
    end6 = result.iloc[i[5]][2]

    start7 = result.iloc[i[6]][1]
    end7 = result.iloc[i[6]][2]

    start8 = result.iloc[i[7]][1]
    end8 = result.iloc[i[7]][2]

    start9 = result.iloc[i[8]][1]
    end9 = result.iloc[i[8]][2]

    start10 = result.iloc[i[9]][1]
    end10 = result.iloc[i[9]][2]
    
    score1= start2-end1
    score2= start3-end2
    score3= start4-end3
    score4= start5-end4
    score5= start6-end5
    score6= start7-end6
    score7= start8-end7
    score8= start9-end8
    score9= start10-end9
    total=score1+score2+score3+score4+score5+score6+score7+score8+score9
    distance=end10-start1


    postotal=0
    negtotal=0
    if score1 > 0:
        postotal += score1
    else:
        negtotal += score1
    if score2 > 0:
        postotal += score2
    else:
        negtotal += score2
    if score3 > 0:
        postotal += score3
    else:
        negtotal += score3
    if score4 > 0:
        postotal += score4
    else:
        negtotal += score4
    if score5 > 0:
        postotal += score5
    else:
        negtotal += score5
    if score6 > 0:
        postotal += score6
    else:
        negtotal += score6      
    if score7 > 0:
        postotal += score7
    else:
        negtotal += score7
    if score8 > 0:
        postotal += score8
    else:
        negtotal += score8 
    if score9 > 0:
        postotal += score9
    else:
        negtotal += score9

    mean= (negtotal+postotal)/9
    ideal= (distance/10)-20
    scores= (score1, score2, score3, score4, score5, score6, score7, score8, score9)
    stdev= statistics.stdev(scores,ideal)

    seqtogether.append ([i, total/distance , stdev, postotal/distance, negtotal/distance, score1, score2, score3, score4, score5, score6, score7, score8, score9])

    # seqtogether.append ([i, df.iloc[i[0]][0],df.iloc[i[1]][0], df.iloc[i[2]][0], start2-end1, start3-end2])

# rankedlist=sorted(seqtogether,key=lambda x: x[3], reverse= True)
rankedlist=sorted(seqtogether,key=lambda x: (x[1], -x[2], x[3],-x[4]), reverse= True)

seq1index= rankedlist[0][0][0]
seq2index= rankedlist[0][0][1]
seq3index= rankedlist[0][0][2]
seq4index= rankedlist[0][0][3]
seq5index= rankedlist[0][0][4]
seq6index= rankedlist[0][0][5]
seq7index= rankedlist[0][0][6]
seq8index= rankedlist[0][0][7]
seq9index= rankedlist[0][0][8]
seq10index= rankedlist[0][0][9]

topresult=[]
topresult.append([result.iloc[seq1index][0],result.iloc[seq2index][0], result.iloc[seq3index][0], result.iloc[seq4index][0], result.iloc[seq5index][0], result.iloc[seq6index][0], result.iloc[seq7index][0], result.iloc[seq8index][0], result.iloc[seq9index][0], result.iloc[seq10index][0]])

# topresult.append([df.iloc[0][0],df.iloc[4][0], df.iloc[5][0], df.iloc[10][0], df.iloc[11][0], df.iloc[12][0], df.iloc[13][0], df.iloc[14][0], df.iloc[15][0], df.iloc[16][0]])


fasta = []
for x in range(0, 10):
    fasta.append("> seq"+str(x+1))
    fasta.append(str(topresult[0][x]))

with open('./output/topresult.txt','w') as f:
    f.write('\n'.join(fasta))

result= pd.DataFrame(rankedlist, columns=["index", "rank1","stdev","rankpos", "rankneg",'score', 'score', 'score', 'score', 'score', 'score', 'score', 'score', 'score'])
result.to_csv(r'.\output\ranked_guides.txt', sep='\t', index=False)
