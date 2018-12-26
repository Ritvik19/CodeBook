for t in range(int(input())):
    D = int(input())
    Ques = [0]*32
    for i in range(D):
        d, p = map(int, input().split())
        Ques[d] = p
    for i in range(1, 32):
        Ques[i] += Ques[i-1]
    Q = int(input())
    for i in range(Q):
        dead, req = map(int, input().split())
        print('Go Sleep') if Ques[dead] < req else print('Go Camp')
