# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have
# a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 
# 1. Each student gets one packet.
# 2 .The difference between the number of chocolates in the packet with maximum chocolates and packet with minimum 
# chocolates given to the students is minimum.

class Solution:
  def findMinDiff(self, A,N,M):
       ans = []
       A.sort()
       for idx in range(N-M+1):
           # 1 3 4 7 9 9 12 56
           # 0 1 2 3 4 5 6  7
           ans.append(A[idx+M-1]-A[idx])
       return min(ans)

# Driver Code
if __name__ == '__main__':
      t = int(input())
      for _ in range(t):
          N = int(input())
          A = [int(x) for x in input().split()]
          M = int(input())
          
          solObj = Solution()
          print(solObj.findMinDiff(A,N,M))
