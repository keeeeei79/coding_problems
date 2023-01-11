BIG_NUM = 2000000000

N, M = map(int, input().split())

table = [BIG_NUM] * (N + 1)  # 0円からN円までに必要な枚数をメモする

table[0] = 0

coin_list = list(map(int, input().split()))

for coin in coin_list:
    for i in range(coin, N + 1):  # そのコインの値から1ずつ大きくしていく
        table[i] = min(table[i], table[i - coin] + 1)
        # 元々計算されていたものか対象のコインを1枚増やした時の小さい方を採用
        # 小さい方から計算していったらcoinを複数枚使った方がいい時は既にcoinを足した方がいいかどうかの問題になる
        # 結局coinを3枚使った方がいいパターンもcoin2枚を使った状態でもう1枚使った方がいいかという問題に帰着する


print("{:d}".format(table[-1]))
