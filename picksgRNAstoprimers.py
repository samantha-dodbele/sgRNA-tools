import pandas as pd
from itertools import combinations 
import csv
import statistics
from xlwt import Workbook
from utils import *

# this function needs sgrna-designs.txt and all_results_together.tab
def sgRNAs(path):

    print (path)
    path1= path+ "/sgrna-designs.txt"
    path2= path + "/all_results_together.tab"

    # Read in CRISPick output file, pick out sgRNA sequences, and write the sgRNAs out to a new csv file
    df = pd.read_csv(path1, sep='\t')
    df.columns = ['crispick' if x == 'sgRNA Sequence' else x for x in df.columns]
    crispick = df['crispick']

    # Read in Ecrisp output file, pick out sgRNA sequences, strip NGG and write the sgRNAs out to a new csv file
    df = pd.read_csv(path2, sep='\t')
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

    outputpath= path+'\output_compare-guides.txt'
    # Combine all dataframes into four columns and write to csv file
    combined = pd.concat([crispick, ecrisp, start, end], join = 'outer', axis = 1) 
    combined.to_csv(outputpath, sep='\t', index = False)

    # Read in txt file that contains crispick and ecrisp guides
    df = pd.read_csv(outputpath, sep='\t')

    # finds the instersection of the crispick and ecrisp sgRNAs and preserves the genome locations associated with the ecrisp list
    intersection = df.merge(df, how = 'inner', left_on = ['crispick'], right_on=['ecrisp'])
    intersection.drop(columns=['crispick_x', 'crispick_y','ecrisp_x','start_x','end_x'], inplace = True)
    intersection.rename(columns={'ecrisp_y': 'Nucleotide sequence', 'start_y': 'Start', 'end_y': 'End'}, inplace = True)

    # write the common sgRNAs and the start and end locations out to a new text file
    outputpath= path+'\output_guide-loc.txt'
    intersection.to_csv(outputpath, sep='\t', index=False)

    # read in the common sgRNAs and thier genome locations
    df = pd.read_csv(outputpath, sep='\t')
    seq= df["Nucleotide sequence"]
    start= df["Start"]
    end= df["End"]

    # Sort the guides by genome location
    result= df.sort_values(by=['Start'])
    outputpath= path+'\output_sorted_guides.txt'
    result.to_csv(outputpath, sep='\t', index=False)

    # calculate all the combinations of ten sgRNAs. If there are less than 10 sgRNAs in common then raise an Exception
    len= seq.size
    if len <10:
        raise Exception ("There are less than 10 common sgRNAs")
    comb = combinations(range(0, len), 10)

    # calculate nine overlap scores for each combination of ten guides 
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

        # calculate negtive and positive overlap scores
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

        # report the combination, the four composite scores, then the nine overlap scores
        seqtogether.append ([i, total/distance , stdev, postotal/distance, negtotal/distance, score1, score2, score3, score4, score5, score6, score7, score8, score9])

    # add these scores to the list ranked list and sort by total distance (large to small), then stdev (small to large), then negtotal/distance (small to large), then posttotal/distance (large to small)
    rankedlist=sorted(seqtogether,key=lambda x: (x[1], -x[2], -x[4], x[3]), reverse= True)

    # assigns the top ranked sgRNA combination to each seq#index
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

    # assigns the top ranked sgRNA combination to top result
    topresult=[]
    topresult.append([result.iloc[seq1index][0],result.iloc[seq2index][0], result.iloc[seq3index][0], result.iloc[seq4index][0], result.iloc[seq5index][0], result.iloc[seq6index][0], result.iloc[seq7index][0], result.iloc[seq8index][0], result.iloc[seq9index][0], result.iloc[seq10index][0]])

    # writes the top result out to a fasta file for viewing in UCSC genome browser
    fasta = []
    for x in range(0, 10):
        fasta.append("> seq"+str(x+1))
        fasta.append(str(topresult[0][x]))

    # write out fasta file of top results
    outputpath= path+'\output_fasta.txt'
    with open(outputpath,'w') as f:
        f.write('\n'.join(fasta))

    # write out text file of chosen guides to generate forward and reverse sgRNA primers
    outputpath= path+'\output_input-guides.txt'
    with open(outputpath,'w') as f:
        inputguides=["Guides"]
        for x in range (0,10):
            inputguides.append(topresult[0][x])    
        f.write('\n'.join(inputguides))

    # writes all the combinations and thier corresponding scores out to a csv file
    result= pd.DataFrame(rankedlist, columns=["index", "rank1","stdev","rankpos", "rankneg",'score', 'score', 'score', 'score', 'score', 'score', 'score', 'score', 'score'])
    outputpath= path+'\output_ranked_guides.txt'
    result.to_csv(outputpath, sep='\t', index=False)

    # read in the common sgRNAs and thier genome locations
    outputpath= path+'\output_input-guides.txt'
    df = pd.read_csv(outputpath, sep='\t')
    guides= df["Guides"]

    # Workbook is created
    wb = Workbook()

    # add_sheet is used to create sheet.
    sheet1 = wb.add_sheet('Sheet 1')

    # add labels in sheet
    sheet1.write(0, 0, "Original sgRNA")
    sheet1.write(0, 1, "Forward Primers (5' to 3')")
    sheet1.write(0, 2, "Reverse Primers (5' to 3')")

    # populate original guide sequence and prepped and checked forward and reverse primers in sheet
    length = guides.size

    # generate forward and reverse primers
    for x in range(0, length):
        seq = str(df["Guides"][x])
        prepped = prep(seq)
        if check_char(prepped) == True:
            sheet1.write(x+1, 0, prepped)
        else:
            sheet1.write(x+1, 0, "Guide contained non ATGC character")

    for x in range(0, length):
        seq = str(df["Guides"][x])
        prepped = prep(seq)
        if check_char(prepped) == True:
            sheet1.write(x+1, 1, get_fwd_primer(prepped))
        else:
            sheet1.write(x+1, 1, "No forward primer ")

    for x in range(0, length):
        seq = str(df["Guides"][x])
        prepped = prep(seq)
        if check_char(prepped) == True:
            sheet1.write(x+1, 2, get_rev_primer(prepped))
        else:
            sheet1.write(x+1, 2, "No reverse primer")

    # write to output file
    outputpath= path+'\output_primers.xls'
    wb.save(outputpath)