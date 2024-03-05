#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Make Changes"""
    if total <= 0:
        return 0

    dp = [0] + [float('inf')] * total

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
