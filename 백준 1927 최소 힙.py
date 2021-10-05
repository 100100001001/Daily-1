# https://www.acmicpc.net/problem/1927

import heapq
import sys

input = sys.stdin.readline

lst = [ int(input()) for _ in range(int(input())) ]
heap = []

for i in lst:
    if i == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, i)