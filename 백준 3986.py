# https://www.acmicpc.net/problem/3986

cnt = 0

for _ in range(int(input())):
    word = input()
    stack = [] 
    for i in word:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    
    if not stack:
        cnt += 1

print(cnt)