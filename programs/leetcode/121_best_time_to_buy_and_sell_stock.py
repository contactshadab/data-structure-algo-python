'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''


# Solution 1: DP
# Run time complexity: O(n)
# Space complexity: O(n)
def max_profit(prices):
    if not prices:
        return 0

    max_profit = 0
    dp = [0 for i in range(len(prices))]
    for i in range(1, len(dp)):
        # If we dont sell on previous day and extend our day, we make dp[i-1] + prices[i] - prices[i-1]
        # If we dont extend our day and start afresh (buy and sell same day) we make 0.
        profit = max(dp[i-1] + prices[i] - prices[i-1], 0)
        dp[i] = profit
        max_profit = max(max_profit, profit)

    return max_profit


# Solution 2
# Run time complexity: O(n)
# Space complexity: O(1)
def max_profit_2(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0
    # dp = [0 for i in range(len(prices))]
    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, prices[i])

    return max_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))
    print(max_profit_2([7, 1, 5, 3, 6, 4]))
