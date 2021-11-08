# https://www.acmicpc.net/problem/14487

n = int(input())
village = list(map(int, input().split()))
print(sum(village) - max(village))