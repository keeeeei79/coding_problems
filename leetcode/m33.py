from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] >= target or nums[l] <= target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


s = Solution()
s.search([5, 1, 3], 5)
s.search([3, 1], 1)
s.search([2], 2)
