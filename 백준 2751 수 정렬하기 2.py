# https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline
lst = [ int(input()) for _ in range(int(input())) ]
lst.sort()
print(*lst, sep='\n')