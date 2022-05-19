# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

class Solution:
 def evalRPN(self, tokens: List[str]) -> int:
    op = {"+":operator.add, "-":operator.sub, "/":operator.truediv, "*":operator.mul}
    stack = []
    for t in tokens:
        if t not in op:
            stack.append(int(t))
        else:
            y = stack.pop()
            x = stack.pop()
            stack.append(int(op[t](x, y)))
    return stack[0]
