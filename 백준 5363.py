# 5363 요다 https://www.acmicpc.net/problem/5363

for _ in range(int(input())):
    sen = input().split()
    print(type(sen))
    print(*sen[2:], *sen[:2])