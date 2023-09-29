def bestSeat(seats):
    best_seat = -1
    max_space = 0

    left = 0
    while left < len(seats):
        right = left + 1
        while right < len(seats) and seats[right] == 0:
            right += 1

        available_space = right - left - 1
        if available_space > max_space:
            print('here')
            best_seat = (left + right) // 2
            max_space = available_space

        left = right

    return best_seat
