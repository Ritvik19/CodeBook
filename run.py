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

hackerrank_stats = []
for folderName, subfolders, filenames in os.walk('data/HackerRank-Statistics//'):
    for filename in filenames:
        hackerrank_stats.append(filename[:-3])
print('HackerRank-Statistics', len(hackerrank_stats))

hackerrank_code = []
for folderName, subfolders, filenames in os.walk('data/HackerRank-Code//'):
    for filename in filenames:
        hackerrank_code.append(filename[:-3])
print('HackerRank-Code', len(hackerrank_code))

programList = pd.DataFrame({
    'Program': codechef+hackerrank_python+hackerrank_js+hackerrank_stats+hackerrank_code,
    'Category': ['CodeChef']*len(codechef)+['HackerRank-Python']*len(hackerrank_python)+['HackerRank-JS']*len(hackerrank_js)+['HackerRank-Statistics']*len(hackerrank_stats)+['HackerRank-Code']*len(hackerrank_code),
    'Language': ['py']*(len(codechef)+len(hackerrank_python))+['js']*len(hackerrank_js)+['py']*(len(hackerrank_stats)+len(hackerrank_code))
}).sort_values('Program').reset_index(drop=True)
print(len(programList))
programList.to_json('data/ProgramList.json')

os.system('surge')
