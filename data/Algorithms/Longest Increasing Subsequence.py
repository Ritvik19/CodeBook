def longestIncreasingSubsequence(nums):
    dp = [1]
    for i in range(1, len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = 1 + dp[j]
    return max(dp)

if __name__ == "__main__":
    print(longestIncreasingSubsequence([3, 2, 6, 4, 5, 7, 1]))
