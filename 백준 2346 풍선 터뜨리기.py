# https://www.acmicpc.net/problem/2346
'''
5
3 2 1 -3 -1
'''

from collections import deque

def popping(balloon):
    answer = []

    while balloon:
        idx, num = balloon.popleft()
        answer.append(idx+1)
        
        if num > 0:
            balloon.rotate(-(num-1))
        else:
            balloon.rotate(-num)

    return answer


_ = int(input())
balloon = deque(enumerate(map(int, input().split())))

print(*popping(balloon))