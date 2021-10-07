# https://www.acmicpc.net/problem/14235

import heapq

n = int(input())
queue = []
for _ in range(n):
    a = input()
    if a == '0':
        if queue:
            print(-heapq.heappop(queue))
        else:
            print(-1)
        # print(-heapq.heappop(queue) if queue else -1)
    else:
        present = list(map(int, a[1:].split()))
        for i in present:
            heapq.heappush(queue, -i)