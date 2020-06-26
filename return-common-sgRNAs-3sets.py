# return common sgRNAs

import pandas as pd

# Read in xlsx file named 'guides' on desktop
df = pd.read_excel(r'.\input\compareguides.xlsx')

list1 = df['Guides'].tolist()
list2 = df['Guides2'].tolist()
list3 = df['Guides3'].tolist()

s_list1 = set(list1)
s_list2 = set(list2)
s_list3 = set(list3)

# sgRNAs in common between all three lists
intersection_1 = s_list1.intersection(s_list2)
intersection_2 = intersection_1.intersection(s_list3)
intersection_as_list = list(intersection_2)

intersection_3 = s_list1.intersection(s_list3)
intersection_4 = s_list2.intersection(s_list3)

# common in between 1 and 2
print("Common in between 1 and 2: "+str(len(intersection_1)))
# common in between 1, 2, and 3
print("Common in between 1, 2, and 3: " + str(len(intersection_2)))
# common in between 1 and 3
print("Common in between 1 and 3: "+str(len(intersection_3)))
# common in between 2 and 3
print("Common in between 2 and 3: "+str(len(intersection_4)))

with open('./output/common_sgrnas.txt', 'w') as f:
    f.write('\n'.join(intersection_as_list))
