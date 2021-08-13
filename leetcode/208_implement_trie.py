# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.eof = '#'
        self.letters = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        level = self.letters
        for letter in word:
            level = level.setdefault(letter, {})
        level[self.eof] = None

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        level = self.letters
        for letter in word:
            if letter in level:
                level = level[letter]
            else:
                return False
        return self.eof in level

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        level = self.letters
        for letter in prefix:
            if letter in level:
                level = level[letter]
            else:
                return False
        return True
