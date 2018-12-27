t, m = input().split()
for i in range(int(t)):
    trans = ''
    W = input()
    for w in W:
        if 'a' <= w <= 'z':
            trans += m[ord(w)-97]
        elif 'A' <= w <= 'Z':
            trans += m[ord(w)-65].upper()
        elif w == '_':
            trans += ' '
        else:
            trans += w
    print(trans)
