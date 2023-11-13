from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 基本線はまずa[k] > a[k+1]となっている箇所を見つけてa[k+1]をreturnする
        # 常にrはk+1までを含むように範囲を決めていく
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if mid < r and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[0]


s = Solution()
s.findMin([4, 5, 1, 2, 3])
# s.findMin([3, 4])
# s.findMin([3, 2])
