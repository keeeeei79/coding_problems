from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[0] <= nums[mid]:
                if target < nums[mid] and target >= nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target < nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()
# s.search([5, 6, 7, 0, 1, 2, 3, 4], 4)
# s.search([5, 6, 7, 0, 1, 2, 3, 4], 2)
# s.search([5, 6, 7, 0, 1, 2, 3, 4], 5)
# s.search([5, 6, 7, 0, 1, 2, 3, 4], 6)
# s.search([4, 5, 6, 7, 0, 1, 2], 0)
# s.search([1, 3], 3)
s.search([5, 1, 3], 5)
