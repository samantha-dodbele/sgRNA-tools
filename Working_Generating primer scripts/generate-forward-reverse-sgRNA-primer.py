# F and R Primers Generator Read in from Excel with Checks
# Original name "ReverseComp_FromExcel_WithChecks_2"

# Guide Excel file should be saved on Desktop and should be labeled "Guides" in cell A1 and then all the guides below it

import pandas as pd
from xlwt import Workbook
from utils import *

# Read in xlsx file named 'guides' on desktop
df = pd.read_excel('.\input\guides.xlsx')

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

# add labels in sheet
sheet1.write(0, 0, "Original sgRNA")
sheet1.write(0, 1, "Forward Primers (5' to 3')")
sheet1.write(0, 2, "Reverse Primers (5' to 3')")

# populate original guide sequence and prepped and checked forward and reverse primers in sheet
length = len(df["Guides"])

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
wb.save('./output/output_primers.xls')

