class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # k番目に大きな数字を返すには1~k番目の数字だけ持っておけばいい
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # heapの大きさは高々+1に収まるので1回pop
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
