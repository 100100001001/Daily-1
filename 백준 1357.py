# 1357 뒤집힌 덧셈 https://www.acmicpc.net/problem/1357

x, y = input().split()
rev = str(int(x[::-1]) + int(y[::-1]))
print(int(rev[::-1]))