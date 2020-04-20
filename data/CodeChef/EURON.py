c=0
def merge(ar1,ar2):
    global c
    m_arr = []
    i=0;j=0
    while (i<len(ar1) and  j<len(ar2)):
        if(ar1[i]<=ar2[j]):
            m_arr.append(ar1[i])
            i+=1
        else:
            m_arr.append(ar2[j])
            c+=len(ar1)-i
            j+=1
    while i<len(ar1):
        m_arr.append(ar1[i])  
        i+=1
    while j<len(ar2):
        m_arr.append(ar2[j])
        j+=1
    return m_arr
    
    
def merge_sort(arr):
    if len(arr)==1:
        return arr
    a1 = arr[:len(arr)//2]
    a2 = arr[len(arr)//2:]
    a1 = merge_sort(a1)
    a2 = merge_sort(a2)
    return merge(a1,a2)

n = int(input())
arr = list(map(int,input().split()))
a = merge_sort(arr)
print(c)