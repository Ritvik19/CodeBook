NO_OF_CHARS = 256


def getNextState(pat, M, state, x):
    if state < M and x == ord(pat[state]):
        return state+1

    i = 0

    for ns in range(state, 0, -1):
        if ord(pat[ns-1]) == x:
            while(i < ns-1):
                if pat[i] != pat[state-ns+1+i]:
                    break
                i += 1
            if i == ns-1:
                return ns
    return 0


def computeTF(pat, M):
    global NO_OF_CHARS

    TF = [[0 for i in range(NO_OF_CHARS)] for _ in range(M+1)]

    for state in range(M+1):
        for x in range(NO_OF_CHARS):
            z = getNextState(pat, M, state, x)
            TF[state][x] = z

    return TF


def search(pat, txt):
    global NO_OF_CHARS
    M = len(pat)
    N = len(txt)
    TF = computeTF(pat, M)

    state = 0
    for i in range(N):
        state = TF[state][ord(txt[i])]
        if state == M:
            print(f"Pattern found at index: {i-M+1}")


def main():
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt)


if __name__ == '__main__':
    main()
