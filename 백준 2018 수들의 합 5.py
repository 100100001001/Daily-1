# https://www.acmicpc.net/problem/2018

n = int(input()) # 15

start = 1
end = 2

total = 3
cnt = 0

while end <= n:
    if total < n:
        end += 1
        total += end

    else:
        if total == n:
            cnt += 1
        start += 1
        total -= start-1

print(cnt)