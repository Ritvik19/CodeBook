import requests

def word2score(word):
    score = 0
    for letter in word.upper():
        score += ord(letter)-64
    return score

names = requests.get('https://projecteuler.net/project/resources/p022_names.txt').text.split(',')
names = list(map(lambda x: x.replace('"', ''), names))
names.sort()
names = list(map(word2score, names))
total_score = 0
for i in range(len(names)):
    total_score += (i+1)*names[i]
print(total_score) # 871198282
