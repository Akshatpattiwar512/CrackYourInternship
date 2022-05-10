# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution(object):
        def calculate(self, s):
            i = 0   ## first index pointer
            op = '' ## operator
            items = [] ## list of number
            
            ## j is the second index pointer
            for j,v in enumerate(s):
                if v == '*' or v == '/' or v == '+' or v == '-' or j+1 == len(s):
                    if j+1 == len(s): ## special handle for last char in input string
                        num1 = int(s[i:].strip())
                    else:
                        num1 = int(s[i:j].strip())
                    if items:
                        if op == '*':
                            num2 = items[-1]
                            del items[-1]
                            items.append(num2*num1)
                        elif op =='/':
                            num2 = items[-1]
                            del items[-1]
                            # handle negative division
                            # 3/2 = 1 but -3/2 = -2
                            if num2 < 0:
                                items.append((-num2/num1)*-1)
                            else:
                                items.append(num2/num1)
                        elif op == '+':
                            items.append(num1)
                        elif op == '-':
                            items.append(-1*num1)
                    ## we meet the first operator, just append the num to list.
                    else:
                        items.append(num1)  
                    op = v
                    i = j+1
            return sum(items)
        
