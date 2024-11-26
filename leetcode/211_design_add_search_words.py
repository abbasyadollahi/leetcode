# https://leetcode.com/problems/design-add-and-search-words-data-structure/


class WordDictionary:
    def __init__(self) -> None:
        """Initialize your data structure here."""
        self.any = "."
        self.eof = "#"
        self.letters = {}

    def addWord(self, word: str) -> None:
        """Inserts a word into the trie."""
        level = self.letters
        for letter in word:
            level = level.setdefault(letter, {})
        level[self.eof] = None

    def search(self, word: str) -> bool:
        """Returns if the word is in the trie."""
        found = False
        num_letters = len(word)
        frames = [(0, self.letters)]
        while frames and not found:
            i, level = frames.pop()
            while i < num_letters:
                letter = word[i]
                i += 1
                if letter in level:
                    level = level[letter]
                elif letter == self.any:
                    frames.extend((i, f) for l, f in level.items() if l != self.eof)
                    if frames:
                        i, level = frames.pop()
                    else:
                        break
                else:
                    break
            else:
                found = self.eof in level
        return found
