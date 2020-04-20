def climb_stairs(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    dp = [0 for i in range(0, n + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    print(climb_stairs(3))
