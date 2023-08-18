class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        t = '0'
        for i in range(n-1):
            t = t.replace('0', 'a')
            t = t.replace('1', 'b')
            t = t.replace('a', '01').replace('b', '10')
        return int(t[k-1])

s = Solution()
print(s.kthGrammar(2,2))