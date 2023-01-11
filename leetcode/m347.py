class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        # 出現回数を基準にkeyのheapを作成
        # 大きさがkになるまでpopして残りが答えになる
        return heapq.nlargest(k, cnt.keys(), key=cnt.get)
