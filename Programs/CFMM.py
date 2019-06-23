for t in range(int(input())):
    n = int(input())
    cauldron = dict()
    for i in range(n):
        S = list(input())
        for s in S:
            if s not in cauldron.keys():
                cauldron[s] = 0
            cauldron[s] += 1
    for elem in 'ceodhf':
        if elem not in cauldron.keys():
            cauldron[elem]=0
    num_meals = 10001
    num_meals = min(num_meals, cauldron['c']//2)
    num_meals = min(num_meals, cauldron['o'])
    num_meals = min(num_meals, cauldron['d'])
    num_meals = min(num_meals, cauldron['e']//2)
    num_meals = min(num_meals, cauldron['h'])
    num_meals = min(num_meals, cauldron['f'])
    print(num_meals)
