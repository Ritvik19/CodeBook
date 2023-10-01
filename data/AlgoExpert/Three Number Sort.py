def threeNumberSort(array, order):
    counts = [0, 0, 0]
    for element in array:
        order_idx = order.index(element)
        counts[order_idx] += 1

    for i in range(3):
        value = order[i]
        count = counts[i]
        num_element_before = sum(counts[:i])
        for n in range(count):
            current_idx = num_element_before + n
            array[current_idx] = value

    return array