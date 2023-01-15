from collections import deque, defaultdict
from typing import List


class Solution:
    def add_word_cands(self, word_converter: dict[str], word: str, length: int) -> None:
        for i in range(length):
            word_converter[word[:i] + "*" + word[i + 1 :]].add(word)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        length = len(beginWord)
        word_converter = defaultdict(set)
        self.add_word_cands(word_converter, beginWord, length)
        for w in wordList:
            self.add_word_cands(word_converter, w, length)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            target_word, level = queue.popleft()
            for i in range(length):
                for w in word_converter[target_word[:i] + "*" + target_word[i + 1 :]]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        visited.add(w)
                        queue.append((w, level + 1))
        return 0


# word_conveterのkeyをword[:i] + "*" + word[i+1:]にすることで探索対象をwordList全体が遷移可能単語のみに限定できる
# BFSを使うため、一度訪れていればもうその単語を探索する必要がないのでvisitedをグローバルに持つようにした

s = Solution()
print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
