import os
# modules to import from the test method
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import function
from test-method import *

directory = 'C:/Users/Samantha/Box Sync/Wilusz Lab/Test'

for root, subdirectories, files in os.walk(directory):
    # print the subdirectory path
    for subdirectory in subdirectories:
        test-method.boxwhisker()