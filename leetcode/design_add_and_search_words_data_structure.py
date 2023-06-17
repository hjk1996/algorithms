#tag: Trie, DFS
#description
'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''


#my solution

class TrieNode:

    def __init__(self):
        self.children = {}
        self.leaf = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()        

    def addWord(self, word: str) -> None:
        # add word to trie
        cur = self.root
        for c in word:
            # if charactor not in children, add it
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # move to next node
            cur = cur.children[c]
        # mark leaf node (end of word)
        cur.leaf = True

    def search(self, word: str) -> bool:
        res = [False]
        def dfs(cur, i):
            # base cases (4)
            # if already found, return 
            if res[0]:
                return 
            # if i is greater than the length of the word and
            # current node is marked as the end of word, update res as True and return:
            if i == len(word) and cur.leaf:
                res[0] = True
                return
            # if i is greater than the length of the word and
            # current node is not marked as the end of word, just end the function
            if i == len(word) and not cur.leaf:
                return
            # if current charactor is not in children and current charactor is not ".", just end the function
            if word[i] != "." and word[i] not in cur.children:
                return
            
            # recursive cases
            # if current charactor is ".", search all children
            if word[i] == ".":
                for child in cur.children:
                    dfs(cur.children[child], i+1)
            # if current charactor is not ".", search the specific child
            else:
                dfs(cur.children[word[i]], i+1)
        
        # do DFS
        dfs(self.root, 0)
        # and return res
        return res[0]

