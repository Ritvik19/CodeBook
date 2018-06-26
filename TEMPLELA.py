for t in range(int(input())):
    n = int(input())
    H = [int(e) for e in input().split()]
    if n%2 == 0:
        print("no")
    else:
        if H[0] != 1:
            print("no")
        else:
            flag = 0
            for i in range(n//2):
                if H[i] != H[n-i-1]:
                    flag = 1
                    break
            if flag == 0:
                for i in range(n//2):
                    if H[i] - H[i+1] != -1:
                        flag = 1
                        break
            if flag == 1:
                print("no")
            else:
                print("yes")
