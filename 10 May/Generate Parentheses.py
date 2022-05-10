# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

class Solution:
    def generateParenthesis(self, n, openCount = 0, closeCount = 0, output = None, temp = None):
        if output is None or temp is None:
            output, temp = [], []
        if len(temp) == 2 * n:
            output.append(''.join(temp))
            return
        if openCount < n:
            temp.append('(')
            openCount += 1
            self.generateParenthesis(n, openCount, closeCount, output, temp)
            temp.pop()
            openCount -= 1
        if closeCount < n and closeCount < openCount:
            temp.append(')')
            closeCount += 1
            self.generateParenthesis(n, openCount, closeCount, output, temp)
            temp.pop()
            closeCount -= 1
        return output
