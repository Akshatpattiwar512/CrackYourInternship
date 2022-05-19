# Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less 
# than or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
# Implement the StockSpanner class:

# StockSpanner() Initializes the object of the class.
# int next(int price) Returns the span of the stock's price given that today's price is price.

class StockSpanner:
    def __init__(self):
        self.data = []
        self.res = []
    def next(self, price: int) -> int:
        self.data.append(price)
        self.res.append(1)
        i = len(self.data) -2
        while i>=0:
            #print(i)
            val = self.data[i]
            if val > self.data[-1]:
                break
            else:
                self.res[-1]+=self.res[i]
                i-=self.res[i]
            #print(i, val)
        return self.res[-1]		

'''
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
'''
