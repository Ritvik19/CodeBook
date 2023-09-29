def sweetAndSavory(dishes, target):
    sweet_dishes = sorted([dish for dish in dishes if dish < 0], key=abs)
    savory_dishes = sorted([dish for dish in dishes if dish > 0])

    best_pair = [0, 0]
    best_diff = float("inf")
    sweet_idx, savory_idx = 0, 0

    while sweet_idx < len(sweet_dishes) and savory_idx < len(savory_dishes):
        current_sum = sweet_dishes[sweet_idx] + savory_dishes[savory_idx]

        if current_sum <= target:
            current_diff = target - current_sum
            if current_diff < best_diff:
                best_diff = current_diff
                best_pair = [sweet_dishes[sweet_idx], savory_dishes[savory_idx]]
            savory_idx += 1
        else:
            sweet_idx += 1

    return best_pair
