class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        ans = []
        max_idx_1 = min(len(nums1), k)
        max_idx_2 = min(len(nums2), k)
        max_ans = min(max_idx_1 * max_idx_2, k)
        # まずnums2はidx=0を固定してnums1の上位k個を調べる
        heap = [
            (nums1[i] + nums2[0], i, 0) for i in range(max_idx_1)
        ]  # TODO: check null
        heapq.heapify(heap)
        ans = []
        while max_ans > 0:
            s, i, j = heapq.heappop(heap)
            ans.append([nums1[i], nums2[j]])
            # nums2のidxを動かした時の値も考える
            # 最小のpairであるi, jが与えられた時、次に最小になるのは(i+1, j) or (i, j+1)
            # ここで(i+1, j)は必ず既にheapに含まれているので(i, j+1)をheapに追加する
            if j + 1 < max_idx_2:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            max_ans -= 1
        return ans
