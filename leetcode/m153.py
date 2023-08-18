from typing import List

# エッジケースが多くだいぶつまづいた
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid - 1]:
                # midが0でもmid[0] < mid[-1]ならrotate=0なので問題ない
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                # これがないとmid=0, r=l+1の時にうまくいかない
                return nums[mid + 1]

            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[0]


s = Solution()
# s.findMin([4, 5, 6, 7, 0, 1, 2])
s.findMin([1])
s.findMin([2, 1])
s.findMin([11, 13, 15, 17])
s.findMin([5, 1, 2, 3, 4])
