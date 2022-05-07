# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == 0:
            return 0
        if k >= len(cardPoints):
            return sum(cardPoints)
        cardPoints = cardPoints[:k] + cardPoints[-k:]
        add_k = 0
        sub_k = 0
        left_k = sum(cardPoints[:k]) 
        right_k = sum(cardPoints[-k:])
        maxsum = max(left_k, right_k)
        for i in range(k):
            add_k += cardPoints[i]
            sub_k += cardPoints[k+i]
            maxsum = max(right_k - sub_k + add_k, maxsum)
        return maxsum
