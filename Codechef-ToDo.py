import pandas as pd
import requests, bs4, os, argparse, sys
from tqdm.auto import tqdm

parser = argparse.ArgumentParser(description="Codechef ToDo Organiser")
parser.add_argument('-c', '--category', metavar='name', 
                    help='name of the category to practise', choices=['b', 'e', 'm', 'h', 'c', 'p'])
parser.add_argument('-s', '--sort', metavar='attribute', 
                    help='sort the problems by an attribute', choices=['n', 'c', 's', 'a'])
parser.add_argument('-r', '--reverse', action='store_true', help='sort in descending order')
args = parser.parse_args()

print('Getting the problems you have solved...')
submitted = []
for folderName, subfolders, filenames in os.walk('data/CodeChef/'):
    for filename in tqdm(filenames):
        submitted.append(filename[:-3])

print()        
url = 'https://www.codechef.com/problems/'

if args.category == 'b':
    url += 'school'
elif args.category == 'e':
    url += 'easy'
elif args.category == 'm':
    url += 'medium'
elif args.category == 'h':
    url += 'hard'
elif args.category == 'c':
    url += 'challenge'
elif args.category == 'p':
    url += 'extcontest'
else:
    print('Provide a valid practise category')
    sys.exit()
    
if args.sort is not None:
    url += '?sort_by='
    if args.sort == 'n':
        url += 'Name'
    elif args.sort == 'c':
        url += 'Code'
    elif args.sort == 's':
        url += 'SuccessfulSubmission'
    elif args.sort == 'a':
        url += 'Accuracy'
    else:
        print('Provide a valid attribute')
        sys.exit()
    if args.reverse == True:
        url += '&sorting_order=desc'
    else:
        url += '&sorting_order=asc'
else:
    pass

problems = {
    'name': [], 'code': [], 'submissions': [], 'accuracy': [], 'status': []
}

res = requests.get(url)

if res.status_code == requests.codes.ok:
    ressoup = bs4.BeautifulSoup(res.text, 'lxml')
    print('Fetching Data')
    for i, td in tqdm(enumerate(ressoup.select('tbody')[0].select('td'))):
        if i % 4 == 0:
            problems['name'].append(td.getText().strip())
        elif i % 4 == 1:
            problems['code'].append(td.getText().strip())
        elif i % 4 == 2:
            problems['submissions'].append(td.getText().strip())
        else:
            problems['accuracy'].append(td.getText().strip())
    print()
    
print('Finding Unsolved Problems')
for code in tqdm(problems['code']):
    problems['status'].append(1) if code in submitted else problems['status'].append(0)
print()

problems = pd.DataFrame(problems)
print('Solved:', problems['status'].sum() ,'/' ,len(problems))

with open('tmp/CodechefToDo.txt', 'w') as f:
    for row in problems[problems['status'] == 0].values:
        f.write(f"{row[0]:50} {row[1]:10} {row[2]:10} {row[3]:5}\n")
        
print('To Do Created')        