def typing(W):
    time = 2
    hand = 'left' if W[0] == 'd' or W[0] == 'f' else 'right'
    for w in W[1:]:
        if (w == 'd' or w == 'f'):
            if hand == 'left':
                time += 2
            hand = 'left'
        if (w == 'j' or w == 'k'):
            if hand == 'right':
                time += 2
            hand = 'right'
        time += 2
    return time

for t in range(int(input())):
    n = int(input())
    words = []
    time = 0
    for i in range(n):
        word = input()
        if word in words:
            time += typing(word)/2
        else:
            time += typing(word)
            words.append(word)
    print(int(time))
