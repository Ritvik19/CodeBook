def compare(l1, l2):
    t=[]
    for j in range(3):
        if(l1[j] < l2[j]):
            t.append(True)
        elif (l1[j] > l2[j]):
            t.append(False)
    for k in range(len(t)):
        if t[0]!=t[k]:
            return False
    return True

for t in range(int(input())):
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))
    s3 = list(map(int, input().split()))
    if s1==s2 or s1==s3 or s2==s3:
        print('no')
    else:
        f1=compare(s1,s2)
        f2=compare(s1,s3)
        f3=compare(s2,s3)
        if f1 and f2 and f3:
            print('yes')
        else:
            print('no')
