for i in range(int(input())):
    y,m,d=map(int,input().strip().split(':'))
    if(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
        print(((31-d)//2)+1)
    elif(m==2):
        if((y%400==0) or (y%100!=0 and y%4==0)):
            print(((29-d)//2)+1)
        else:
            print(((59-d)//2)+1)
    else:
        print(((61-d)//2)+1)
