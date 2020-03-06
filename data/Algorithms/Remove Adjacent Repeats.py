def removeAdjacentRepeats(string):
    string = list(string)
    i = 1
    while i < len(string):
        while string[i] == string[i-1] and i > 0:
            string.pop(i)
            string.pop(i-1)
            i = max(0, i-2)
        i += 1
    return ''.join(string)
    
if __name__ == '__main__':
    string = 'qdwbbeeccwdaa'    
    print(removeAdjacentRepeats(string))