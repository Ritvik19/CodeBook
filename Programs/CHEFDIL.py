for t in range(int(input())):
    s= list(input())
    print("LOSE") if s.count('1') % 2 == 0 else print("WIN")
        
