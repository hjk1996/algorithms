#tag: graph, bfs
#description
'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


'''
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        graph = defaultdict(list)

        # build graph
        for w in wordList:
            for i in range(len(w)):
                # create pattern by replacing single letter with *
                pattern = w[:i] + "*" + w[i+1:]
                # map pattern to word
                graph[pattern].append(w)

        # bfs
        visited = set()
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    # find all adjacent words by pattern
                    pattern = word[:j] + "*" + word[j+1:]
                    for adj in graph[pattern]:
                        # if adjacent word is not visited, add it to queue
                        if adj not in visited:
                            visited.add(adj)
                            q.append(adj)
            res += 1
        
        return 0
        


