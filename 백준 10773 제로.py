# https://www.acmicpc.net/problem/10773

from collections import deque
import sys

stack = deque()
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))