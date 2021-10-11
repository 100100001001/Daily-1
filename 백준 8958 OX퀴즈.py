# https://www.acmicpc.net/problem/8958

N = int(input())
for i in range(N):
    num = input()
    score = 0
    count = 0
    for j in range(len(num)):
        if num[j] == 'O':
            count += 1
            score += count
        elif num[j] == 'X':
            count = 0
    print(score)