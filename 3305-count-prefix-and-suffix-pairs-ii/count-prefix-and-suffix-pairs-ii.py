class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = dict()
        self.idx = -1
        self.cnt = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int):
        node = self.root
        res = defaultdict(int)
        for i, c in enumerate(word):
            if c in node.children:
                node = node.children[c]
                if node.is_word:
                    res[node.idx] = node.cnt
            else:
                node.children[c] = TrieNode()
                node = node.children[c]
                
        node.is_word = True
        node.idx = idx
        node.cnt += 1
        # return a dict key is previous idx, value is count
        return res
    
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # for all pairs i<j, need check with prefix and suffix, 
        # Trie! during insert: get the qualified index pairs...
        
        arr = [(i, w) for i, w in enumerate(words)]
        
        trie0 = Trie()
        trie1 = Trie()
        res = 0
        for idx, w in arr:
            # handle prefix
            pre = trie0.insert(w, idx)
            
            # handle suffix
            suf = trie1.insert(w[::-1], idx)
                        
            for k in pre:
                res += min(pre[k], suf[k])
        
        return res