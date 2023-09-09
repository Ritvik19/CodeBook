# O(n log n) O(1)

def nonConstructibleChange(coins):
    coins.sort()

    current_change_created = 0
    for coin in coins:
        if coin > current_change_created + 1:
            return current_change_created + 1

        current_change_created += coin
    return current_change_created +  1

nonConstructibleChange(**{
  "coins": [1, 5, 1, 1, 1, 10, 15, 20, 100]
})