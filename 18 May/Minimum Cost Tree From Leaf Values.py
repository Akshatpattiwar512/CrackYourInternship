# Given an array arr of positive integers, consider all binary trees such that:

# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

# A node is a leaf if and only if it has zero children.

import sys
class Solution(object):
    def mctFromLeafValues(self, arr):
        ans = 0
        while(len(arr) > 1):
            n = len(arr)
            temp = sys.maxsize
            index = 0
            for i in range(n-1):
                mul = arr[i] * arr[i+1]
                if(mul < temp):
                    index = i
                    temp = mul
            ans += temp
            if(arr[index] < arr[index+1]):
                arr.pop(index)
            else:
                arr.pop(index+1)
        return(ans)
