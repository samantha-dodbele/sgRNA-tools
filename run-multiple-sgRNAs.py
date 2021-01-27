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

directory = 'C:/Users/Samantha/Box Sync/Wilusz Lab/Test'

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        # print(os.path.join(root, subdirectory))
        sgRNAs(os.path.join(root, subdirectory))