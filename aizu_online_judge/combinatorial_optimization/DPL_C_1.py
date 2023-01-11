N, W = map(int, input().split())
goods_list = [list(map(int, input().split())) for _ in range(N)]
table = [0] * (W + 1)

# そのgoodsを候補に加えた時、重さwを考える時w
for (v, w) in goods_list:
    for i in range(w, W + 1):
        table[i] = max(table[i], table[i - w] + v)

print("{:d}".format(table[-1]))
