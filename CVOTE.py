n, m = map(int, input().split())
countries = {}      #chef to country
chefvotes = {}      #chef to vote
countryvotes = {}    #country to vote

for i in range(n):
    chef, country = input().split()
    countries[chef] = country
    chefvotes[chef] = 0
    countryvotes[country] = 0
for i in range(m):
    chef = input()
    chefvotes[chef] += 1
    countryvotes[countries[chef]] += 1

chefvotes = sorted(chefvotes, key = chefvotes.get, reverse = True)
countryvotes = sorted(countryvotes, key = countryvotes.get, reverse = True)

print(countryvotes[0])
print(chefvotes[0])
