for t in range(int(input())):
    n = int(input())
    s = input()
    x, y = 0, 0
    refined = []
    if len(s) > 0:
        refined = s[0]
        for i in range(1,len(s)):
            if (refined[-1] == "L" or refined[-1] == "R") and (s[i] == "U" or s[i] == "D"):
                refined = refined + s[i]
            elif (refined[-1]=="U" or refined[-1]=="D") and (s[i]=="L" or s[i]=="R"):
                refined = refined + s[i]

        for i in range(len(refined)):
            if refined[i]=="L":
                x=x-1
            elif refined[i]=="R":
                x=x+1
            elif refined[i]=="U":
                y=y+1
            else:
                y=y-1
    print(x,y)