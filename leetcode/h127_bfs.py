from collections import deque, defaultdict
from typing import List


class Node:
    def __init__(self, val: str, visited: set[str]):
        self.val = val
        self.visited = visited


class Solution:
    def make_word_cands(self, word_converter: dict[str], word: str, length: int) -> None:
        for i in range(length):
            word_converter[word[:i] + "*" + word[i+1:]].add(word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        word_converter = defaultdict(set)
        self.make_word_cands(word_converter, beginWord, length)
        for w in wordList:
            self.make_word_cands(word_converter, w, length)

        queue = deque([Node(beginWord, set())])
        while queue:
            node = queue.popleft()
            visited = node.visited.copy()
            visited.add(node.val)
            for i in range(length):
                for w in word_converter[node.val[:i] + "*" + node.val[i+1:]]
                    if w == endWord:
                        return len(visited) + 1
                    if w not in node.visited:
                        queue.append(Node(w, visited))
        return 0
    
# visitedをnode毎に管理する必要がない

