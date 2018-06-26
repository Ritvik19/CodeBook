def alpha(alphabet, word):
    for letter in word:
        if letter not in alphabet:
            return "No"
    return "Yes"

alphabet = input()
for i in range(int(input())):
    print(alpha(alphabet, input()))
