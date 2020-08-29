class Node:
    def __init__(self, exists, children):
        self.exists = exists
        self.children = children

class Trie:

    def __init__(self):
        self.root = Node(False, {});
    

    def insert(self, word: str) -> None:
        d = self.root
        for i, c in enumerate(word):
            if c not in d.children:
                d.children[c] = Node(False, {})
            
            d = d.children[c]
        
        d.exists = True
        

    def search(self, word: str) -> bool:
        d = self.root
        for c in word:
            if c not in d.children:
                return False
            
            d = d.children[c]
            
        return d.exists
        

    def startsWith(self, prefix: str) -> bool:
        d = self.root
        for c in prefix:
            if c not in d.children:
                return False
            
            d = d.children[c]        
        
        return True
