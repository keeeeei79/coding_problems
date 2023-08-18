class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_v = 0
        seen = {} # 見た文字列のindexを格納する
        l = 0
        for r in range(len(s)):
            if s[r] not in seen:
                # そもそも見ていないならmaxを更新
                max_v = max(max_v, r-l+1)
            else:
                if seen[s[r]] < l:
                    # 見たけど今のlよりも左なら問題ないのでlを更新
                    max_v = max(max_v, r-l+1)
                else:
                    # l~rの中で2回目を見てしまったのでその文字列の1回目を飛ばすところまでlを動かす
                    l = seen[s[r]] + 1
            seen[s[r]] = r # 見たindexを格納する
        return max_v
