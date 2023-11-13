import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        res = []
        heapq.heapify(res)
        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(res, (-n1 - n2, [n1, n2]))
                if len(res) > k:
                    total, arr = heapq.heappop(res)
                    if total == -n1 - n2:
                        break
        return [x[1] for x in res]
