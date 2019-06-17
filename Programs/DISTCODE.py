for t in range(int(input())):
    S = input()
    codes = []
    for i in range(len(S)-1):
        codes.append(S[i:i+2])
    print(len(set(codes)))
