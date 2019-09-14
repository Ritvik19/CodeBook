import pandas as pd
import os

codechef = []
for folderName, subfolders, filenames in os.walk('CodeChef/'):
    for filename in filenames:
        codechef.append(filename[:-3])

hackerrank_python = []
for folderName, subfolders, filenames in os.walk('HackerRank-Python//'):
    for filename in filenames:
        hackerrank_python.append(filename[:-3])

programList = pd.DataFrame({
    'Program': codechef+hackerrank_python,
    'Category': ['CodeChef']*len(codechef)+['HackerRank-Python']*len(hackerrank_python)
}).sort_values('Program').reset_index(drop=True)
print(len(programList))
programList.to_json('ProgramList.json')
