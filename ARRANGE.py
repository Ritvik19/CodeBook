for t in range(int(input())):
    n, word = input().split()
    n= int(n)
    length = 2**n
    new_word = ""
    for i in range(length):
        binary = "{0:b}".format(i, n)
        if len(binary) < n:
            binary = "0"*(n-len(binary)) + binary
        pos = int(binary[::-1], 2)
        new_word += word[pos]
    print(new_word)
