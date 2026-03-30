class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        stack = [(self.root,0)]
        while len(stack):
            curr, i = stack.pop()
            if i == len(word) and curr.word:
                return True
            elif i >= len(word):
                continue
            c = word[i]
            if c != "."  and c not in curr.children:
                continue
            elif c == ".":
                for child in curr.children:
                    stack.append((curr.children[child], i + 1))
            else:
                stack.append((curr.children[c], i + 1))
        return False

