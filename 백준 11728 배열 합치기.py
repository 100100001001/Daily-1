# https://www.acmicpc.net/problem/11728

import sys
input = sys.stdin.readline

_ = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []

a_idx = 0
b_idx = 0

while a_idx != len(a) or b_idx != len(b): 
    if a_idx == len(a):
        answer.append(b[b_idx])
        b_idx += 1
    elif b_idx == len(b):
        answer.append(a[a_idx])
        a_idx += 1
    else:
        if a[a_idx] < b[b_idx]:
            answer.append(a[a_idx])
            a_idx += 1
        else:
            answer.append(b[b_idx])
            b_idx += 1
    
print(*answer)