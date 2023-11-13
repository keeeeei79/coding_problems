from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 直接days以内に運ぶための最小のcapacityを二部探索する
        l = max(weights)
        r = sum(weights)
        ans = r
        while l <= r:
            mid = (l + r) // 2
            cumsum = 0
            day = 1
            for w in weights:
                if cumsum + w <= mid:
                    cumsum += w
                else:
                    day += 1
                    cumsum = w
            if day <= days:
                r = mid - 1
                ans = mid
            else:
                l = mid + 1
        return ans


s = Solution()
s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
