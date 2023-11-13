class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # iまでの合計とjまでの合計の差がkならsum(nums[i+1]~nums[j])=kになる
        # nums[j]について考えた時、過去にnums[j]-kの値を持つnums[i]が存在していればi~jの配列の合計がkになる
        d = defaultdict(int)
        d[0] = 1
        cnt = 0
        total = 0
        for n in nums:
            total += n
            cnt += d[total - k]
            d[total] += 1
        return cnt
