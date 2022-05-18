#Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.

class MyStack(object):
    def __init__(self):
        self.l = list()
    def push(self, x):
        self.l.append(x)
    def pop(self):
        holder = self.l[-1]
        self.l[:] = self.l[:-1]
        return holder
    def top(self):
        return self.l[-1]
    def empty(self):
        return len(self.l) == 0
        
'''
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
'''
