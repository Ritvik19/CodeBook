def minion_game(word):
    vowels = set('AEIOU')
    stuart = kevin = 0
    for i, c in enumerate(word):
        if c in vowels:
            kevin += len(word) - i
        else:
            stuart += len(word) - i
    if stuart > kevin:
        print('Stuart', stuart)
    elif kevin > stuart:
        print('Kevin', kevin)
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
