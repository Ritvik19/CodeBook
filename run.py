import pandas as pd
import os, sys, json

programList = []

count_loc = 0
count_for = 0
count_while = 0
count_if = 0
count_asgnmt = 0


for folderName, subfolders, filenames in os.walk('E:/Coding/CodeBook/data/'):
    for filename in filenames:
        *fname, extension = filename.split('.')
        fname = '.'.join(fname)
        dname = folderName.split('/')[-1]
        if extension != 'json':
            with open(f'{folderName}/{filename}') as f:
                data = f.read()
                count_loc += len(data.split('\n'))
                count_asgnmt += data.count(' = ')
                count_for += data.count('for')
                count_while += data.count(('while'))
                count_if += data.count('if')
                
        programList.append((fname, extension, dname))
programList.pop(0)
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

json.dump(({'loc': count_loc, 'expressions': count_asgnmt, 'for': count_for,
            'while': count_while, 'decisions': count_if}), open('data/ProgramAnalysis.json', 'w'))

os.system('surge')
c = sys.argv[1]
os.system('git add .')
os.system(f'git commit -m "Commit {c}"')
os.system('git push origin master')
