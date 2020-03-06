class Node():
    lo = None
    hi = None
    eq = None
    endpoint = False

    def __init__(self, char):
        self.char = char

    def __repr__(self):
        return ''.join(['[', self.char,
                        ('' if not self.endpoint else ' <end>'),
                        ('' if self.lo is None else ' lo: ' + self.lo.__repr__()),
                        ('' if self.eq is None else ' eq: ' + self.eq.__repr__()),
                        ('' if self.hi is None else ' hi: ' + self.hi.__repr__()), ']'])


def insert(node, string):
    if len(string) == 0:
        return node

    head = string[0]
    tail = string[1:]
    if node is None:
        node = Node(head)

    if head < node.char:
        node.lo = insert(node.lo, string)
    elif head > node.char:
        node.hi = insert(node.hi, string)
    else:
        if len(tail) == 0:
            node.endpoint = True
        else:
            node.eq = insert(node.eq, tail)

    return node


def search(node, string):
    if node is None or len(string) == 0:
        return False

    head = string[0]
    tail = string[1:]
    if head < node.char:
        return search(node.lo, string)
    elif head > node.char:
        return search(node.hi, string)
    else:
        # use 'and' for matches on complete words only,
        # versus 'or' for matches on string prefixes
        if len(tail) == 0 or node.endpoint:
            return True
        return search(node.eq, tail)


def suffixes(node):
    if node is not None:
        if node.endpoint:
            yield node.char

        if node.lo:
            for s in suffixes(node.lo):
                yield s
        if node.hi:
            for s in suffixes(node.hi):
                yield s
        if node.eq:
            for s in suffixes(node.eq):
                yield node.char + s


def autocompletes(node, string):
    if node is None or len(string) == 0:
        return []

    head = string[0]
    tail = string[1:]
    if head < node.char:
        return autocompletes(node.lo, string)
    elif head > node.char:
        return autocompletes(node.hi, string)
    else:
        if len(tail) == 0:
            return suffixes(node.eq)
        return autocompletes(node.eq, string[1:])


class Trie():
    root = None

    def __init__(self, string):
        self.append(string)

    def append(self, string):
        self.root = insert(self.root, string)

    def __contains__(self, string):
        return search(self.root, string)

    def autocomplete(self, string):
        return map(lambda x: string + x, autocompletes(self.root, string))

if __name__ == "__main__":
    trie = Trie('cute')
    trie.append('cup')
    trie.append('at')
    trie.append('as')
    trie.append('he')
    trie.append('us')
    trie.append('i')
    print(trie.root)
    print('cup' in trie)
    print('cups' in trie)
    print('cute' in trie)
