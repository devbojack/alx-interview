#!/usr/bin/python3
"""Make changes within"""


def makeChange(coins, total):
    """Make changes within"""
    if total <= 0:
        return 0

    # Initialize memoization table with -1
    memo = [-1] * (total + 1)

    def dp(target):
        # Base case: if the target is 0, no coins are needed
        if target == 0:
            return 0

        # If the result is already calculated, return it from the memoization table
        if memo[target] != -1:
            return memo[target]

        # Initialize the result to a large value
        result = float('inf')

        # Iterate through each coin
        for coin in coins:
            # If the coin value is less than or equal to the target, recursively calculate the result
            if coin <= target:
                sub_result = dp(target - coin)
                # If the sub-result is valid and better than the current result, update the result
                if sub_result >= 0 and sub_result < result:
                    result = sub_result + 1

        # If no valid result is found, set the memoization value to -1
        memo[target] = result if result != float('inf') else -1
        return memo[target]

    # Call the dynamic programming function with the given total
    return dp(total)
