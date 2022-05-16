# https://www.acmicpc.net/problem/1100

cnt = 0

for j in range(8):
    chess = input()

    for i in range(8):
        if j % 2 == 0:
            if i % 2 == 0 and chess[i] == 'F':
                cnt += 1
        else:
            if i % 2 != 0 and chess[i] == 'F':
                cnt += 1

print(cnt)