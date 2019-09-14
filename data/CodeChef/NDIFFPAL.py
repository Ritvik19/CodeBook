for t in range(int(input())):
    Palindrome = list()
    letters = 'abc'
    h = 0
    for i in range(int(input())):
        Palindrome.append(letters[h])
        h = (h+1)%3
    Palindrome = ''.join(Palindrome)
    print(Palindrome)
