#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution(object):
    def reverse(self, x):
        rev=0
        max_int,min_int=(1<<31)-1,-(1<<31)
        def cdiv(a,b):
            return int(float(a)/b)
        def cremainder(a,b):
            return a-cdiv(a,b)*b
        while x!=0:
            tmp=cdiv(x,10) # x//10=floor(float(x)/10), wrong
            pop= x-tmp*10 #x%10 positive, wrong
            x=tmp
            if rev>cdiv(max_int,10) or (rev==cdiv(max_int,10) and pop>7): return 0
            if rev<cdiv(min_int,10) or (rev==cdiv(min_int,10) and pop<-8):return 0
            rev=rev*10+pop
        return rev
