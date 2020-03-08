def printInterleavings(str1, str2):
    perms = []
    if len(str1) + len(str2) == 1:
        return [str1 or str2]
    if str1:
        for item in printInterleavings(str1[1:], str2):
            perms.append(str1[0] + item)
    if str2:
        for item in printInterleavings(str1, str2[1:]):
            perms.append(str2[0] + item)
    return perms


if __name__ == '__main__':
    print(*printInterleavings("AB", "CD"), sep="\n")
