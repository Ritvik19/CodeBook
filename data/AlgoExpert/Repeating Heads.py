def repeating_heads(n, x):
    win_chance = 0.5 ** n
    lose_chance = 1 - win_chance

    repeated_lose_chance = lose_chance ** x
    repeated_win_chance = 1 - repeated_lose_chance

    break_even_payout = 100 / repeated_win_chance

    return [repeated_win_chance * 100, break_even_payout]