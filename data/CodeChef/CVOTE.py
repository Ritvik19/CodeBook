N, M = map(int, input().split())
chefCountry = {}
chefVotes = {}
countryVotes = {}
for i in range(N):
    name, country = (input().split())
    chefCountry[name] = country
    chefVotes[name] = 0
    countryVotes[country] = 0
for i in range(M):
    a = input()
    chefVotes[a] += 1
    countryVotes[chefCountry[a]] += 1
winnerChef = []
winnerCountry = []
maxVote = 0
for i in countryVotes.keys():
    maxVote = max(maxVote, countryVotes[i])
for i in countryVotes.keys():
    if countryVotes[i] == maxVote:
        winnerCountry.append(i)
print(min(winnerCountry))
maxVote = 0
for i in chefVotes.keys():
    maxVote = max(maxVote, chefVotes[i])
for i in chefVotes.keys():
    if chefVotes[i] == maxVote:
        winnerChef.append(i)

print(min(winnerChef))