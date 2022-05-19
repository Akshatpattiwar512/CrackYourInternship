# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an 
# iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

'''
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """
'''
class NestedIterator:    
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = []
        while nestedList:      
            if nestedList[0].isInteger():
                self.nestedList.append(nestedList[0].getInteger())
                nestedList.pop(0)
            elif nestedList[0].getList() != []:
                k = nestedList[0].getList()
                nestedList.pop(0)
                nestedList = k + nestedList
            else:
                nestedList.pop(0)              
    def next(self) -> int: 
        return self.nestedList.pop(0)     
    def hasNext(self) -> bool:
        if len(self.nestedList) >= 1:
            return True
        else:
            return False
         
'''
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
'''
