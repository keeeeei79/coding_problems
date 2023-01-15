from typing import List


class Node:
    def __init__(self, val: str, visited: set[str]):
        self.val = val
        self.visited = visited


class Solution:
    def calc_char_diff(self, s1: str, s2: str) -> int:
        cnt = 0
        for x, y in zip(s1, s2):
            if x != y:
                cnt += 1
        return cnt

    def search(
        self, node: Node, wordList: List[str], endWord: str, res: List[Node]
    ) -> None:
        candidates = [
            w
            for w in wordList
            if w not in node.visited and self.calc_char_diff(node.val, w) == 1
        ]
        if not candidates:
            return
        visited = node.visited.copy()
        visited.add(node.val)
        if endWord in candidates:
            res.append(Node(endWord, visited))
            return
        for cand in candidates:
            cand_node = Node(cand, visited)
            self.search(cand_node, wordList, endWord, res)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        node = Node(beginWord, set())
        res: List[Node] = []
        self.search(node, wordList, endWord, res)
        return min([len(x.visited) for x in res]) + 1 if res else 0


# DFSだとTimeOutになる
# BFSで見つかった時点で探索を終了する必要がある
