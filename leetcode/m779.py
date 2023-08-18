# 0
# 0 1
# 0 1  1 0
# 0 1  1 0  1 0  0 1


# n=4でk=3を求める時には、n=3のk=2が1なら1で0なら0になる
# n=4でk=4を求める時には、n=3のk=2が1なら0で0なら1になる
# n=4でk=7を求める時には、n=3のk=4が1なら1で0なら0になる

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 0:
            return 1 if self.kthGrammar(n-1, (k+1)//2) == 0 else 0
        return 0 if self.kthGrammar(n-1, (k+1)//2) == 0 else 1

s = Solution()
print(s.kthGrammar(2,2))
