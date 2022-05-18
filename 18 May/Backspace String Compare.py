# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def simplify(s):
            stack = []
            simple_string = []
            for char in s[::-1]:
                if char == '#':
                    stack.append('#')
                else:
                    if stack:
                        stack.pop()
                    else:
                        simple_string.append(char)
            return ''.join(simple_string[::-1])
        return simplify(S) == simplify(T)
