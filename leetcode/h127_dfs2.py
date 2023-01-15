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

    def search(self, node: Node, wordList: List[str], endWord: str) -> List[int]:
        # endWordまでの距離を返すようにする
        candidates = [
            w
            for w in wordList
            if w not in node.visited and self.calc_char_diff(node.val, w) == 1
        ]
        if not candidates:
            return []
        visited = node.visited.copy()
        visited.add(node.val)
        if endWord in candidates:
            return [len(visited) + 1]
        res = []
        for cand in candidates:
            cand_node = Node(cand, visited)
            res += self.search(cand_node, wordList, endWord)
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        node = Node(beginWord, set())
        res = self.search(node, wordList, endWord)
        return min(res) if res else 0


# DFSだとTimeOutになる
# searchでendWordまでの距離を返すようにする
# こっちだとimmutableになる
