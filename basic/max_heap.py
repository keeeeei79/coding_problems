def get_parent_idx(i: int) -> int:
    return int(i / 2)


def get_left_child_idx(i: int) -> int:
    return i * 2


def get_right_child_idx(i: int) -> int:
    return i * 2 + 1


def maxHeapify(i: int, A: list[int]):
    lidx = get_left_child_idx(i)
    ridx = get_right_child_idx(i)

    if lidx <= H and A[lidx] > A[i]:
        largest = lidx
    else:
        largest = i

    if ridx <= H and A[ridx] > A[largest]:
        largest = ridx

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(largest, A)


H = int(input())
a = list(map(int, input().split()))
A = [-1] + a  # 扱いやすいように1-originにする

# 子を持つ節点の中で最大のものから逆順に適用
# 子を持つ節点の中で最大のものは最後のnodeの親になるので
# get_parent_idx(H)すればいい
for idx in range(get_parent_idx(H), 0, -1):
    maxHeapify(idx, A)

print(A[1:])

# Example
## Input
# 10
# 4 1 3 2 16 9 10 14 8 7
## Output
# [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
