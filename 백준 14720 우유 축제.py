# https://www.acmicpc.net/problem/14720

_ = int(input())
store = list(map(int, input().split()))

cnt = 0

for i in store:
    if i == cnt % 3:
        cnt += 1
print(cnt)