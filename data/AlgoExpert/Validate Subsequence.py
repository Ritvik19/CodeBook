# O(n) O(1)

def isValidSubsequence(array, sequence):
    matches = 0
    for element in array:
        if sequence[matches] == element:
            matches += 1
        if matches == len(sequence):
            return True
    return matches == len(sequence)

isValidSubsequence(**{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, 10]
})