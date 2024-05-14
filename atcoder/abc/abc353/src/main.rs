use proconio::input;
use std::collections::hash_map::HashMap;

struct TrieNode {
    children: HashMap<char, TrieNode>,
    cnt: i32,
}

impl TrieNode {
    fn new() -> Self {
        Self {
            children: HashMap::new(),
            cnt: 0,
        }
    }
}

struct Trie {
    root: TrieNode,
}

impl Trie {
    fn new() -> Self {
        Self {
            root: TrieNode::new(),
        }
    }
    fn insert(&mut self, word: &str) {
        let mut node = &mut self.root;
        for c in word.chars() {
            if !node.children.contains_key(&c) {
                node.children.insert(c, TrieNode::new());
            }
            node = node.children.get_mut(&c).unwrap();
        }
        node.cnt += 1;
    }
    fn traverse_trie(&self) -> i32 {
        self._traverse_trie(&self.root, 0, 0)
    }
    fn _traverse_trie(&self, node: &TrieNode, acc: i32, depth: i32) -> i32 {
        let mut ans = 0;
        ans += acc * node.cnt;
        dbg!(node.cnt, depth);
        for node in node.children.values() {
            ans += self._traverse_trie(node, acc + (node.cnt * depth), depth + 1);
        }
        ans
    }
}

fn main() {
    input! {
        n: i32,
        mut S: [String; n],  // Vec<(i32, i32, i32)>
    }
    let mut trie = Trie::new();
    for s in S {
        trie.insert(&s);
    }
    let ans = trie.traverse_trie();
    println!("{}", ans);
}
