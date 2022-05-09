# RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing 
# specific elements and also removing a random element.

# Implement the RandomizedCollection class:

#RandomizedCollection() Initializes the empty RandomizedCollection object.
#bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
#bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in
#the multiset, we only remove one of them.
#int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of same
#values the multiset contains.
#You must implement the functions of the class such that each function works on average O(1) time complexity.

#Note: The test cases are generated such that getRandom will only be called if there is at least one item in the RandomizedCollection.

class RandomizedCollection(object):
    def __init__(self):
        self.dOfd = collections.defaultdict(dict)
        self.d = collections.defaultdict(list)
        self.a = []
    def insert(self, val):
        self.d[val].append(len(self.a))
        self.dOfd[val][len(self.a)] = len(self.d[val]) - 1
        self.a.append(val)
        return len(self.d[val]) == 1
    def remove(self, val):
        dd = self.dOfd
        a = self.a
        d = self.d
        if not d[val]:
            return False
        idx = d[val][-1]
        a[idx] = a[-1]
        idxInDForLast = dd[a[-1]][len(a) - 1]
        d[a[-1]][idxInDForLast] = idx
        dd[a[-1]][idx] = idxInDForLast
        del dd[a[-1]][len(a) - 1]
        d[val].pop()
        a.pop()
        return True
    def getRandom(self):
        return self.a[random.randrange(0, len(self.a))]
