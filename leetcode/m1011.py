from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 直接days以内に運ぶための最小のcapacityを二部探索する
        left = max(weights)
        right = sum(weights)
        while left < right:
            # capacityがmidで運べるのかを調べる
            mid = (left + right) // 2
            cumsum = 0
            day = 1
            for w in weights:
                if cumsum + w > mid:
                    day += 1
                    cumsum = 0
                cumsum += w
            if day > days:
                left = mid + 1
            else:
                right = mid
        return left
