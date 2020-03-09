def change(S, m, n):
    """
    Recurrsive Solution
    Arguments:
        S {[list]} -- [Set of coins]
        m {[int]} -- [length of set of coins]
        n {[int]} -- [amount]
    Returns:
        Number of ways to make change
    """
    if (n == 0):
        return 1

    if (n < 0):
        return 0

    if (m <= 0 and n >= 1):
        return 0

    return change(S, m - 1, n) + change(S, m, n-S[m-1])
    
def change(S, m, n):
    """
    Dynamic Programming    
    Arguments:
        S {[list]} -- [Set of coins]
        m {[int]} -- [length of set of coins]
        n {[int]} -- [amount]
    Returns:
        Number of ways to make change
    """
    table = [[0 for x in range(m)] for x in range(n+1)]

    for i in range(m):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
    return table[n][m-1]
    
if __name__ == "__main__":
    arr = [1, 2, 3]
    print(change(arr, len(arr), 4))
