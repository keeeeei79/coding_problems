from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DPっぽさを考えると
        # s[i]までうまくいってるかどうかを確認するなら
        # s[:j]がうまくいってる and s[j:i]がwordDictに含まれることを使う
        # s[:j]がうまくいってるかは計算済みのはず
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i, -1, -1):
                if dp[j] and s[j : i + 1] in wordDict:
                    dp[i + 1] = True
                    break
        return dp[-1]


s = Solution()
s.wordBreak("applepenapple", ["apple", "pen"])
