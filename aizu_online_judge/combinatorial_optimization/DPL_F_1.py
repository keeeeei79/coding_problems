N, W = map(int, input().split())
all_v = 0
all_w = 0
goods_list = []
for _ in range(N):
    v, w = list(map(int, input().split()))
    goods_list.append([v, w])
    all_v += v
    all_w += w

table = [all_w] * (all_v + 1)
table[0] = 0

# Wがめっちゃ大きいのでO(NV)の方向で考える
# 価値iを作るときに自分が入らない場合と入る場合でどっちのが合計のwが小さくなるかを考える
# (価値iが作れない時はでかい数字が入ってる)
# min(table[i], table[i - v] + w)
# i-vにvの価値を足せば必ず価値がiになる
for (v, w) in goods_list:
    for i in range(all_v, v - 1, -1):
        table[i] = min(table[i], table[i - v] + w)

print("{:d}".format(max([i for i in range(len(table)) if table[i] <= W])))
