prices = []
for n in range(int(input())):
    prices.append(int(input()))

prices.sort(reverse=True)
revenue = [a*(i+1) for i, a in enumerate(prices)]
print(max(revenue))