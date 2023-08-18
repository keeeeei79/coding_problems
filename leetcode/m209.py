from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        output = len(nums) + 1
        for r in range(len(nums)):
            # targetより大きくなるまでrを動かす
            target -= nums[r]
            # targetより大きくなったらlを1つずつ右に動かしtargetより小さくならない範囲を求める
            while target <= 0:
                output = min(output, r-l+1)
                target += nums[l]
                l += 1
        return output % (len(nums)+1) # outputがupdateされてないと0が帰る

s = Solution()
s.minSubArrayLen(7,[2,3,1,2,4,3])