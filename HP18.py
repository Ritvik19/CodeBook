for t in range(int(input())):
    n, a, b = map(int, input().split())
    A = list(map(int, input().split()))
    nc = 0  # number of numbers diviible by both a and b
    na = 0  # number of numbers diviible by both a not b
    nb = 0  # number of numbers diviible by both b not a
    # swap a and b because a is the lucky number of BOB
    a, b = b, a
    for i in A:
        if i%a == 0 and i%b == 0:
            nc += 1
        elif i%a == 0 and i%b != 0:
            na += 1
        elif i%a != 0 and i%b == 0:
            nb += 1
    winner = 'BOB' if nb > na else 'ALICE' if nc == 0 else 'BOB' if nb >= na else 'ALICE'
    print(winner)
