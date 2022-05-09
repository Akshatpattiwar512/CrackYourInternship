# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

class Solution:
    def isValid(self, s: str) -> bool:
        
        hasmap = {')' : '(', ']' : '[', '}' : '{'}
        stack = []
        for st in s : 
            if st in ['(', '[', '{'] : 
                stack.append(st)
            elif stack : 
                item = stack.pop()
                if item != hasmap[st]  : 
                    return False
            else : 
                return False
        
        if not stack : 
            return True
        else : 
            return False
