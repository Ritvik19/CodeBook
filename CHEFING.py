for t in range(int(input())):
    sp_ing = set('qwertyuiopasdfghjklzxcvbnm')
    for i in range(int(input())):
        sp_ing = sp_ing & set(input())
    print(len(sp_ing))
