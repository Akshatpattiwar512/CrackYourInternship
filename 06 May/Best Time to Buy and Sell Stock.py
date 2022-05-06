# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
	def maxProfit(self, prices: List[int]) -> int:

		min_value = min(prices)
		bought = prices[prices.index(min_value):]

		max_value = max(bought)


		if max_value > min_value:
			profit = max_value - min_value
		else:
			profit = 0

		return profit
