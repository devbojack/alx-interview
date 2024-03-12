#!/usr/bin/python3
"""Prime Game"""


def findMultiples(num, targets):
    """Finds multiples of a given number
    within a list and removes them.
    """
    for i in targets.copy():
        if i % num == 0:
            targets.remove(i)
    return targets


def isPrime(i):
    """Check if a number is prime
    """
    if i == 1:
        return False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            return False
    return True


def findPrimes(n):
    """Finds prime numbers in a set and
    removes their multiples
    """
    counter = 0
    target = list(n)
    for i in target.copy():
        if isPrime(i):
            counter += 1
            target.remove(i)
            target = findMultiples(i, target)
    return counter


def isWinner(x, nums):
    """Determines the winner of each round of
    the prime game"""
    players = {'Maria': 0, 'Ben': 0}
    for elem in range(x):
        cluster = set()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
        temp = findPrimes(cluster)
        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
