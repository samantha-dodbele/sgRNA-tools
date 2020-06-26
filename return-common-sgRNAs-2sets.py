# return common sgRNAs

import pandas as pd

# Read in xlsx file named 'guides' on desktop
df = pd.read_excel(r'.\input\compareguides.xlsx')

list1 = df['Guides'].tolist()
list2 = df['Guides1'].tolist()

s_list1 = set(list1)
s_list2 = set(list2)

# sgRNAs in common between all three lists
intersection_1 = s_list1.intersection(s_list2)
intersection_as_list = list(intersection_1)

# common in between 1 and 2
print("Common in between 1 and 2: "+str(len(intersection_1)))

with open('./output/common_sgrnas.txt', 'w') as f:
    f.write('\n'.join(intersection_as_list))
