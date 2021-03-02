import pandas as pd
from xlwt import Workbook
from utils import *
import os

def compileprimers (path):
    path1= path+"/output_8-primers.xls"
    df = pd.read_excel(path1, sep='\t')
    forward= df["Forward Primers (5' to 3')"]
    reverse= df["Reverse Primers (5' to 3')"]

    forward.to_csv('C:/Users/Samantha/Box Sync/Wilusz Lab/Completed/CRISPRI/forward-primers.csv', mode='a', header=False, index = False)
    reverse.to_csv('C:/Users/Samantha/Box Sync/Wilusz Lab/Completed/CRISPRI/reverse-primers.csv', mode='a', header=False, index = False)

directory = 'C:/Users/Samantha/Box Sync/Wilusz Lab/Completed/CRISPRI'

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        compileprimers(os.path.join(root, subdirectory))
