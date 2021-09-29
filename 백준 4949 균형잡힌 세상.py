# https://www.acmicpc.net/problem/4949

from collections import deque

while True:
    sen = input()
    if sen == '.':
        break
    stack = deque()
    temp = True
    for i in sen:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if temp == True and not stack:
        print('yes')
    else:
        print('no')
        