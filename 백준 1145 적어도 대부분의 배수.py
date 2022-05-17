# https://www.acmicpc.net/problem/1145

lst = list(map(int, input().split()))
n = 1

while True:
    cnt = 0
    for i in lst:
        if n % i == 0:
            cnt += 1
    
    if cnt >= 3:
        break
    else:
        n += 1

print(n)