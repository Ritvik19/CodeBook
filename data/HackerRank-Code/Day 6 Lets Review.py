# Enter your code here. Read input from STDIN. Print output to STDOUT
for t in range(int(input())):
    S = input()
    Se = ''
    So = ''
    for i in range(len(S)):
        if i%2 == 0:
            Se += S[i]
        else:
            So += S[i]
    print(Se, So)
