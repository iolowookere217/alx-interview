#!/usr/bin/python3
from typing import List


def makeChange(coins: List, total: int) -> int:
    sorted_coins = sorted(coins, reverse=True)
    used_coins = 0

    for coin in sorted_coins:
        if total == 0:
            break
        used_coins += total // coin
        total = total % coin

    if total == 0:
        return used_coins
    return -1
