from typing import Tuple

class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.counter = 1
    

def add(root, word: str):
    """
    Adding a word in the trie structure
    """
    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of the present `node`
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another
                # word has it as well
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break
        # We did not find it so add a new chlid
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node
    # Everything finished. Mark it as the end of a word.
    node.word_finished = True


def find_max(root, word: str) -> Tuple[bool, int]:
    node = root
    ans = 0
    for char in word:
      for child in node.children:
          if child.char == char:
              node = child
              break

      if node.counter == 1:
          break

      ans += 1

    return ans


N = int(input())
t = TrieNode('*')
S = []
for _ in range(N):
  s = input()
  add(t, s)
  S.append(s)

for s in S:
  print(find_max(t, s))