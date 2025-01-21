from typing import List

"""121. Best Time to Buy and Sell Stock
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104"""


# Solution 1
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_diff = float("-inf")
        for buy in range(len(prices)):
            for sell in range(buy + 1, len(prices)):
                if prices[buy] < prices[sell]:
                    diff = prices[sell] - prices[buy]
                    if diff > 0:
                        max_diff = max(max_diff, diff)

        return max_diff if max_diff > float("-inf") else 0


s1 = Solution1()
# print(s1.maxProfit([7, 1, 5, 3, 6, 4]))
# Time O(N" 2)
# Space O(1)


# Solution 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit


s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
