class PriorityQueue:
    H = 0
    A = [-1] * 10  # 手抜きで10個までメモリを確保しとく

    def get_parent_idx(self, i: int) -> int:
        return int(i / 2)

    def get_left_child_idx(self, i: int) -> int:
        return i * 2

    def get_right_child_idx(self, i: int) -> int:
        return i * 2 + 1

    def maxHeapify(self, i: int):
        lidx = self.get_left_child_idx(i)
        ridx = self.get_right_child_idx(i)

        if lidx <= self.H and self.A[lidx] > self.A[i]:
            largest = lidx
        else:
            largest = i

        if ridx <= self.H and self.A[ridx] > self.A[largest]:
            largest = ridx

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.maxHeapify(largest)

    def extract(self) -> int:
        if self.H < 1:
            return -1
        maxv = self.A[1]
        self.A[1] = self.A[self.H]
        self.H -= 1
        self.maxHeapify(1)
        return maxv

    def increaseKey(self, i: int, key: int):
        self.A[i] = key
        # 親と比較してそれより大きければ入れ替える
        while i > 1 and self.A[i] > self.A[self.get_parent_idx(i)]:
            self.A[i], self.A[self.get_parent_idx(i)] = (
                self.A[self.get_parent_idx(i)],
                self.A[i],
            )
            i = self.get_parent_idx(i)

    def insert(self, key: int):
        self.H += 1
        self.A[self.H] = -1
        self.increaseKey(self.H, key)


pq = PriorityQueue()

cmds = []
while True:
    input_line = input()
    if input_line:
        cmds.append(input_line)
    else:
        break

for s in cmds:
    if s == "end":
        break
    elif s.startswith("insert"):
        pq.insert(int(s.split()[-1]))
    else:
        print(pq.extract())

# Example
## Input
# insert 8
# insert 2
# extract
# insert 10
# extract
# insert 11
# extract
# extract
# end

## Output
# 8
# 10
# 11
# 2
