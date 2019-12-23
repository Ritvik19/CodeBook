import pandas as pd
import os

programList = []

for folderName, subfolders, filenames in os.walk('E:/Coding/CodeBook/data/'):
    for filename in filenames:
        *fname, extension = filename.split('.')
        fname = '.'.join(fname)
        dname = folderName.split('/')[-1]
        programList.append((fname, extension, dname))
programList.pop(0)

programList = pd.DataFrame(programList, columns=['Program', 'Language', 'Category']).sort_values('Program').reset_index(drop=True)
print(len(programList))
programList.to_json('data/ProgramList.json')
print(programList['Category'].value_counts())
os.system('surge')
c = int(input())
os.system('git add .')
os.system('git commit -m "Commit {c}"')
os.system('git push origin master')
