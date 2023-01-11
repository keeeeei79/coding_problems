N = int(input())
A = list(map(int, input().split()))

s_A = sorted(A)

# 自分までの合計で隣と合体できるか
best_i = N - 1
cum_arr = [0] * N
for i in range(N - 1):
    cum = cum_arr[i] + s_A[i]
    cum_arr[i + 1] = cum
    nxt = s_A[i + 1]
    if cum * 2 >= nxt:
        if i < best_i:
            best_i = i
    else:
        best_i = N - 1
print(N - best_i)
