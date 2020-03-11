import pandas as pd
import os, sys, json
from collections import defaultdict

histogram = defaultdict(lambda : 0)
programList = []

count_loc = 0
count_for = 0
count_while = 0
count_until = 0
count_foreach = 0
count_if = 0
count_asgnmt = 0
count_prog = 0


for folderName, subfolders, filenames in os.walk('E:/Coding/CodeBook/data/'):
    for filename in filenames:
        *fname, extension = filename.split('.')
        fname = '.'.join(fname)
        dname = folderName.split('/')[-1]
        if extension != 'json':
            if extension != 'txt':
                count_prog += 1
                with open(f'{folderName}/{filename}') as f:
                    data = f.read()
                    histogram[len(data.split('\n'))//10] += 1
                    count_loc += len(data.split('\n'))
                    count_asgnmt += data.count(' = ')
                    count_for += data.count('for')
                    count_while += data.count(('while'))
                    count_until += data.count('until')
                    count_foreach += data.count('foreach')
                    count_foreach += data.count('forEach')
                    count_if += data.count('if')                
            programList.append((fname, extension, dname))

programList = pd.DataFrame(programList, columns=['Program', 'Language', 'Category']).sort_values('Program').reset_index(drop=True)
print(len(programList))
programList.to_json('data/ProgramList.json')
print(programList['Category'].value_counts())
programList['Category'].value_counts().to_json('data/ProgramCounts.json')
print(programList['Language'].value_counts().drop('txt'))
programList['Language'].value_counts().drop('txt').to_json('data/ProgramLanguage.json')
json.dump(({'loc': count_loc, 'expressions': count_asgnmt, 'for': count_for, 'foreach': count_foreach, 'until': count_until,
            'while': count_while, 'decisions': count_if, 'num': count_prog}), open('data/ProgramAnalysis.json', 'w'))
json.dump(histogram, open('data/ProgramHistogram.json', 'w'))
os.system('surge')
c = sys.argv[1]
os.system('git add .')
os.system(f'git commit -m "Commit {c}"')
os.system('git push origin master')
