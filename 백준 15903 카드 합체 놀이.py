# https://www.acmicpc.net/problem/15903

import heapq
import sys

input = sys.stdin.readline

_, m = map(int, input().split())
card_list = list(map(int, input().split()))

heapq.heapify(card_list)

for _ in range(m): 
    card1 = heapq.heappop(card_list)
    card2 = heapq.heappop(card_list)

    heapq.heappush(card_list, card1 + card2) 
    heapq.heappush(card_list, card1 + card2)

print(sum(card_list))