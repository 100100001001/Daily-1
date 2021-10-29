# https://www.acmicpc.net/problem/11004

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
print(lst[k-1])