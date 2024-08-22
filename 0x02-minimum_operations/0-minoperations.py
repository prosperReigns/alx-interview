#!/usr/bin/python3
""" Minimum Operations"""


def minOperations(n):
    """
    Function to calculate the minimum number of operations
    needed to result in exactly n 'H' characters in the file.

    :param n: The target number of 'H' characters
    :return: The minimum number of operations needed,
    or 0 if n is impossible to achieve
    """
    if n < 1:
        return 0
    if n == 1:
        return 0

    # Initialize the dp array with a large number
    dp = [float('inf')] * (n + 1)
    dp[1] = 0  # Base case: it takes 0 operations to get 1 H

    for i in range(2, n + 1):
        # Check all divisors of i
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                # j is a divisor
                dp[i] = min(dp[i], dp[j] + (i // j))
                # i // j is also a divisor
                dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n]
