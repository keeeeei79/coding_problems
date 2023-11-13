class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(set)
        for w in [beginWord] + wordList:
            self.convertToDic(w, d)

        queue = [[beginWord, 1]]
        visited = set([beginWord])
        while queue:
            bw, count = queue.pop(0)
            for i in range(len(bw)):
                cands = d[bw[:i] + "*" + bw[i + 1 :]]
                for c in cands:
                    if c in visited:
                        continue
                    if c == endWord:
                        return count + 1
                    queue.append([c, count + 1])
                    visited.add(c)
        return 0

    # あらかじめ{"*ot": {"hot", "dot", "lot"}}というdictを作る
    def convertToDic(self, w, d):
        for i in range(len(w)):
            d[w[:i] + "*" + w[i + 1 :]].add(w)
