from typing import List

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         self.wordSet = set(wordDict)
#         return self.checkHead(s)

#     def checkHead(self, txt: str):
#         if len(txt) == 0:
#             return True
#         for i in range(len(txt) + 1):
#             if txt[:i] in self.wordSet:
#                 if self.checkHead(txt[i:]):
#                     return True
#         return False


# dp[i]はi番目までの文字列でうまくいっているかどうか
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                # dp[j]までの文字列でうまくいってる and それ以降もwordSetに入ってる
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[-1]


s = Solution()
s.wordBreak("leetcode", ["leet", "code"])
