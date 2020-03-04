class TrieNode(): 
    def __init__(self): 
        self.children = [None]*26
        self.isEndOfWord = False
  
class Trie: 
    def __init__(self): 
        self.root = self.getNode() 

    def getNode(self): 
        return TrieNode() 

    def _charToIndex(self,ch): 
        return ord(ch)-ord('a') 

    def insert(self,key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 

            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 

        pCrawl.isEndOfWord = True

    def search(self, key): 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 

        return pCrawl != None and pCrawl.isEndOfWord 

if __name__ == '__main__': 
    keys = ["the","a","there","anaswe","any", "by","their"] 
    output = ["Not present in trie", "Present in trie"] 
    t = Trie() 
    for key in keys: 
        t.insert(key) 
    for query in ["the", "these", "their", "thaw"]:
        print(query, "-", output[t.search(query)])