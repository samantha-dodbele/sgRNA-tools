import os
# import modules needed from picksgRNAstoprimers.py
import pandas as pd
from itertools import combinations 
import csv
import statistics
from xlwt import Workbook
from utils import *
# import method sgRNAs
from picksgRNAstoprimers import sgRNAs

directory = 'C:/Users/Samantha/Box Sync/Wilusz Lab/sgRNAs'

log=[]
for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        
        log.append(subdirectory)
        log.append(sgRNAs(os.path.join(root, subdirectory)))
        errorlogpath= directory+'/Error-Log.txt'

        # write the error log out to a new txt file 
        file = open(errorlogpath, 'w+', newline ='') 
        with file:     
            write = csv.writer(file) 
            write.writerows(log)         