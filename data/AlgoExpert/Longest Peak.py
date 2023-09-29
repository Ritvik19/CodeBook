def longestPeak(array):
    longest_peak = 0
    i = 1
    while i < len(array) - 1:
        is_peak = array[i-1] < array[i] and array[i] > array[i+1]
        if not is_peak:
            i += 1
            continue

        left = i - 2
        while left >= 0 and array[left] < array[left + 1]:
            left -= 1

        right = i + 1
        while right < len(array) and array[right] < array[right - 1]:
            right += 1

        current_peak = right - left - 1
        longest_peak = max(longest_peak, current_peak)
        i = right

    return longest_peak
