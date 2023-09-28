# O(n) | O(n)

def firstDuplicateValue(array):
    seen = set()
    for val in array:
        if val in seen:
            return val
        seen.add(val)
    return -1
