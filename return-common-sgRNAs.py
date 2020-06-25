# return common sgRNAs

import pandas as pd

# Read in xlsx file named 'guides' on desktop
df = pd.read_excel(r'.\input\compareguides.xlsx')

list1 = df['Guides'].tolist()
list2 = df['Guides2'].tolist()
#list3 = df['Guides3'].tolist()

s_list1 = set(list1)
s_list2 = set(list2)
#s_list3 = set(list3)

intersection_1 = s_list1.intersection(s_list2)
#intersection_2 = intersection_1.intersection(s_list3)
#intersection_as_list = list(intersection_2)
intersection_as_list = list(intersection_1)


with open('./output/common_sgrnas.txt', 'w') as f:
    f.write('\n'.join(intersection_as_list))
