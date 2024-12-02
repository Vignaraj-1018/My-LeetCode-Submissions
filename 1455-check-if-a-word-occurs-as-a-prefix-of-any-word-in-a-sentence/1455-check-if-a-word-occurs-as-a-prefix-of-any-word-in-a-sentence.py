class TrieNode:
    def __init__(self, index = -1):
        self.idx = index
        self.children = {}

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def trieInsert(self, word, index):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode(index)
            curr = curr.children[ch]
            # curr.idx = index

    def trieSearch(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return -1
            curr = curr.children[ch]
        return curr.idx

    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for i, word in enumerate(words):
            self.trieInsert(word, i + 1)
        return self.trieSearch(searchWord)