'''
Source: AlgoExpert

Given an array of positive integers representing coin denominations and a
single non-negative integer n representing a target amount of
money, write a function that returns the smallest number of coins needed to
make change for (to sum up to) that target amount using the given coin
denominations.

Note that you have access to an unlimited amount of coins. In other words, if the denominations are [1, 5, 10] , you have access to an unlimited amount of 1, 5 and 10s
Input: n=7, arr = [1, 5, 10]
Output = 3
'''


def min_number_of_coins_for_change(n, denoms):
    coins = [float('inf') for i in range(n+1)]
    coins[0] = 0

    for d in denoms:
        for amount in range(1, n+1):
            if d <= amount:
                coins[amount] = min(coins[amount], 1 + coins[amount - d])

    return coins[n] if coins[n] != float('inf') else -1


if __name__ == "__main__":
    print(min_number_of_coins_for_change(3, [1, 5, 10]))
