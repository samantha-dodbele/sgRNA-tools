import pandas as pd
from itertools import combinations 
import csv
import statistics
from xlwt import Workbook
from utils import *

# this function needs sgrna-designs.txt and all_results_together.tab
def sgRNAs(path):

    path1= path+ "/sgrna-designs.txt"
    path2= path + "/all_results_together.tab"
    log=[]

    # First try catch for reading the two guides in and writing out all the sgRNAs from both
    try:
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
        log.append ("Success...output_compare-guides.txt")

    except:
        log.append ("Fail...output_compare-guides.txt")

    # Second try catch for reading in both sets of sRNAs and writing out the sgRNAs in common
    try:
        # Read in txt file that contains crispick and ecrisp guides
        df = pd.read_csv(outputpath, sep='\t')

        # finds the instersection of the crispick and ecrisp sgRNAs and preserves the genome locations associated with the ecrisp list
        intersection = df.merge(df, how = 'inner', left_on = ['crispick'], right_on=['ecrisp'])
        intersection.drop(columns=['crispick_x', 'crispick_y','ecrisp_x','start_x','end_x'], inplace = True)
        intersection.rename(columns={'ecrisp_y': 'Nucleotide sequence', 'start_y': 'Start', 'end_y': 'End'}, inplace = True)

        # write the common sgRNAs and the start and end locations out to a new text file
        outputpath= path+'\output_guide-loc.txt'
        intersection.to_csv(outputpath, sep='\t', index=False)
        log.append ("Success...output_guide-loc.txt")
    except:
        log.append ("Fail...output_guide-loc.txt")

    # third try catch for reading in common sgRNAs and writing out sorted by genome location
    try:
        # read in the common sgRNAs and thier genome locations
        df = pd.read_csv(outputpath, sep='\t')
        seq= df["Nucleotide sequence"]
        start= df["Start"]
        end= df["End"]

        # Sort the guides by genome location
        result= df.sort_values(by=['Start'])
        outputpath= path+'\output_sorted_guides.txt'
        result.to_csv(outputpath, sep='\t', index=False)
        log.append ("Success...output_sorted_guides.txt")
    except:
        log.append ("Fail...output_sorted_guides.txt")

    return log