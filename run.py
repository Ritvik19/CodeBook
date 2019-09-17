import pandas as pd
import os

codechef = []
for folderName, subfolders, filenames in os.walk('data/CodeChef/'):
    for filename in filenames:
        codechef.append(filename[:-3])
print('CodeChef', len(codechef))

hackerrank_python = []
for folderName, subfolders, filenames in os.walk('data/HackerRank-Python//'):
    for filename in filenames:
        hackerrank_python.append(filename[:-3])
print('HackerRank-Python', len(hackerrank_python))

hackerrank_js = []
for folderName, subfolders, filenames in os.walk('data/HackerRank-JS//'):
    for filename in filenames:
        hackerrank_js.append(filename[:-3])
print('HackerRank-JS', len(hackerrank_js))

programList = pd.DataFrame({
    'Program': codechef+hackerrank_python+hackerrank_js,
    'Category': ['CodeChef']*len(codechef)+['HackerRank-Python']*len(hackerrank_python)+['HackerRank-JS']*len(hackerrank_js),
    'Language': ['py']*(len(codechef)+len(hackerrank_python))+['js']*len(hackerrank_js)
}).sort_values('Program').reset_index(drop=True)
print(len(programList))
programList.to_json('data/ProgramList.json')

os.system('surge')
