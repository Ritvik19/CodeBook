def merge_the_tools(s, k):
    i = 0
    map, to_print = {}, ""
    while i < len(s):
        if i % k == 0 and i != 0:
            print(to_print)
            map, to_print = {}, ""
        if s[i] not in map.keys():
            map[s[i]] = 0
            to_print += s[i]
        i += 1
    print(to_print)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
