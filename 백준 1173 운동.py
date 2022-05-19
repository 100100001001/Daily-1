# https://www.acmicpc.net/problem/1173

N, m, M, T, R = map(int, input().split())
x = m
ans = 0

while N > 0:
    if m + T > M:
        ans = -1
        break

    if x + T <= M:
        ans += 1
        x += T
        N -= 1
    else:
        ans += 1
        x -= R
        if x < m:
            x = m

print(ans)