def minNumberOfCoinsForChange(n, denoms):
    num_coins = [float("inf") for _ in range(n+1)]
    num_coins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                num_coins[amount] = min(num_coins[amount], num_coins[amount - denom] + 1)
    return num_coins[n] if num_coins[n] != float("inf") else -1