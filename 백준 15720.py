# 백준 15720 카우버거 https://www.acmicpc.net/problem/15720

n = list(map(int, input().split()))

burger = sorted(list(map(int, input().split())), reverse=True)
side = sorted(list(map(int, input().split())), reverse=True)
drink = sorted(list(map(int, input().split())), reverse=True)

discount = 0
for i in range(min(n)):
    discount += int((burger[i] + side[i] + drink[i]) * 0.1)

before = sum(burger) + sum(side) + sum(drink)
print(before)
print(before - discount)