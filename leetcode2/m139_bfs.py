from typing import List

# Timeout
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # iまでで成立しているかを調べる
        wordDict = set(wordDict)
        maxLength = max([len(x) for x in wordDict])
        queue = [s]
        while queue:
            x = queue.pop(0)
            if x == "":
                return True
            for i in range(1, min(len(x), maxLength) + 1):
                if x[:i] in wordDict:
                    queue.append(x[i:])
        return False


s = Solution()
s.wordBreak("applepenapple", ["apple", "pen"])
