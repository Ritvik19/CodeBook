def bina(n, m):
    rep = bin(n)[2:]
    pad = m - len(rep)
    return pad * " " + rep


def inta(n, m):
    rep = str(n)
    pad = m - len(rep)
    return pad * " " + rep + " "


def octa(n, m):
    rep = oct(n)[2:]
    pad = m - len(rep)
    return pad * " " + rep + " "


def hexa(n, m):
    rep = hex(n)[2:].upper()
    pad = m - len(rep)
    return pad * " " + rep + " "

def print_formatted(n):
    m = len(bin(n).lstrip("0b"))
    for i in range(1, n+1):
        r = [inta(i, m), octa(i, m), hexa(i, m), bina(i, m)]
        print("".join(r))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
