def just_smaller(a, e):
    pos = -1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (high+low)//2
        if a[mid] <= e:
            pos = a[mid]
            low = mid + 1
        else:
            high = mid - 1
    return pos

def just_greater(a, e):
    pos = -1
    low = 0
    high = len(a)-1
    while low <= high:
        mid = (high+low)//2
        if a[mid] >= e:
            pos = a[mid]
            high = mid - 1
        else:
            low = mid + 1
    return pos 
    
if __name__ == '__main__':
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81]
    print('Just Smaller', just_smaller(a, 19))
    print('Just Greater', just_greater(a, 19))