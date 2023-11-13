from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [[beginWord, 1]]
        visited = set([beginWord])
        while queue:
            bw, count = queue.pop(0)
            for w in wordList:
                if w in visited:
                    continue
                if not self.canTransition(bw, w):
                    continue
                if w == endWord:
                    return count + 1
                queue.append([w, count + 1])
                visited.add(w)
        return 0

    def canTransition(self, p: str, n: str) -> bool:
        count = 0
        for c1, c2 in zip(p, n):
            if c1 != c2:
                count += 1
            if count > 1:
                return False
        return count == 1


s = Solution()
s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
