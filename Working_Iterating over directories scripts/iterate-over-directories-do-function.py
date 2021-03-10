import os
# modules to import from the test method
import pandas as pd

# import function
from testmethod import test

rootdir = 'C:/Users/Samantha/Box Sync/Wilusz Lab/Test'


for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        print (os.path.join(subdir, file))
        
        # test(os.path.join(subdir, file))