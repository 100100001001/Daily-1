# https://www.acmicpc.net/problem/15969

_ = input()
lst = list(map(int, input().split()))
print(max(lst) - min(lst))