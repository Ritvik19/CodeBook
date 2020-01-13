import pandas as pd
import os, sys

programList = []

for folderName, subfolders, filenames in os.walk('E:/Coding/CodeBook/data/'):
    for filename in filenames:
        *fname, extension = filename.split('.')
        fname = '.'.join(fname)
        dname = folderName.split('/')[-1]
        programList.append((fname, extension, dname))
programList.pop(0)
programList.pop(0)
programList.pop(0)

programList = pd.DataFrame(programList, columns=['Program', 'Language', 'Category']).sort_values('Program').reset_index(drop=True)
print(len(programList))
programList.to_json('data/ProgramList.json')
print(programList['Category'].value_counts())
programList['Category'].value_counts().to_json('data/ProgramCounts.json')
print(programList['Language'].value_counts())
programList['Language'].value_counts().to_json('data/ProgramLanguage.json')
os.system('surge')
c = sys.argv[1]
os.system('git add .')
os.system(f'git commit -m "Commit {c}"')
os.system('git push origin master')
