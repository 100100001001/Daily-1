# https://www.acmicpc.net/problem/3986

cnt = 0

for _ in range(int(input())):
    word = input()
    stack = [] 
    for i in word:
        if len(stack) == 0:
            stack.append(i)
        elif len(stack) >= 1:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    
    if len(stack) == 0:
        cnt += 1

print(cnt)