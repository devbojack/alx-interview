#!/usr/bin/python3
"""Make changes within
"""


def makeChange(coins, total):
    """Changes within"""
    if total <= 0:
        return 0

    # Dictionary to store the minimum number of coins for each amount
    dp = {}

    def minCoins(amount):
        """Min coins"""
        if amount == 0:
            return 0
        if amount < 0:
            return float('inf')
        if amount in dp:
            return dp[amount]
        min_coins = min(minCoins(amount - coin) + 1 for coin in coins)
        dp[amount] = min_coins
        return min_coins

    result = minCoins(total)
    return result if result != float('inf') else -1
