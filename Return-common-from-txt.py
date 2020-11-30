# return common sgRNAs

import pandas as pd

# Read in txt file that contains crispick and ecrisp guides
df = pd.read_csv(r'.\input\compareguides.txt', sep='\t')

list1 = df['crispick'].tolist()
list2 = df['ecrisp'].tolist()

s_list1 = set(list1)
s_list2 = set(list2)

# sgRNAs in common between all three lists
intersection_1 = s_list1.intersection(s_list2)
intersection_as_list = list(intersection_1)

# common in between 1 and 2
print("Common in between 1 and 2: "+str(len(intersection_1)))

with open('./output/common_sgrnas.txt', 'w') as f:
    f.write('\n'.join(intersection_as_list))
