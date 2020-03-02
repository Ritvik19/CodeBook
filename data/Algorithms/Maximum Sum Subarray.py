def maxCrossingSum(arr, l, m, h):
    sm = 0
    left_sum = -10000

    for i in range(m, l-1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm

    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

    return left_sum + right_sum

def maxSubArraySum(arr, l, h):
    if (l == h):
        return arr[l]
    m = (l + h) // 2
    return max(maxSubArraySum(arr, l, m), maxSubArraySum(arr, m+1, h), maxCrossingSum(arr, l, m, h))

if __name__ == '__main__':
    arr = [2, 3, -8, 5, 7]
    n = len(arr)
    print("Maximum contiguous sum is ", maxSubArraySum(arr, 0, n-1))
