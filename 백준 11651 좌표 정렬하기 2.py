# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline

coordination = [ input().split() for _ in range(int(input())) ]
coordination = sorted(coordination, key=lambda x: [int(x[1]), int(x[0])])

for i in coordination:
    for j in i:
        print(int(j), end=' ')
    print(end='\n')