for t in range(int(input())):
    n = int(input())
    population = [1,0,0]
    for i in range(3, n+1):
        x = i % 26
        if x == 3:
            population[0], population[1] = population[1], population[0]
        if x == 11:
            population[1], population[2] = population[2], population[1]
        if x == 1:
            population[2], population[0] = population[0], population[2]
            population[0] *= 2
    print(*population)
