import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count.keys():
                count[n] += 1
            else:
                count[n] = 1

        res = []
        heapq.heapify(res)
        for n, cnt in count.items():
            heapq.heappush(res, (cnt, n))
            if len(res) > k:
                heapq.heappop(res)
        return [x[1] for x in res]
