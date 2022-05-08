# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

class Solution:
    def recur_match(self, board, m, n, row, col, word, word_index):       
        letter = board[row][col]            
        if letter == word[word_index]:
            if word_index == len(word) - 1:
                return True
        else:
            return False
        
        # avoid reuse
        board[row][col] = None
        
        # move up
        if 0 <= row - 1 and self.recur_match(board, m, n, row - 1, col, word, word_index + 1):
            return True
        # move down
        if row + 1 < m and self.recur_match(board, m, n, row + 1, col, word, word_index + 1):
            return True
        # move left
        if 0 <= col - 1 and self.recur_match(board, m, n, row, col - 1, word, word_index + 1):
            return True
        # move right
        if col + 1 < n and self.recur_match(board, m, n, row, col + 1, word, word_index + 1):
            return True
        
        # allow reuse by other path
        board[row][col] = letter
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        # let m x n be #rows x #cols
        m = len(board)
        n = len(board[0])
        
        # O(1)
        if len(word) > m * n:
            return False

        # worst case O(4^k), k is len(word)
        for row in range(m):
            for col in range(n):
                if self.recur_match(board, m, n, row, col, word, 0):
                    return True
        return False
