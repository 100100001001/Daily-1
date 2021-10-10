# https://www.acmicpc.net/problem/1065

N = int(input())

count = 0
for i in range(1, N+1):
    lst = list(map(int, str(i)))
    if i < 100:
        count += 1
    elif lst[0] - lst[1] == lst[1] - lst[2]:
        count += 1
print(count)