# https://www.acmicpc.net/problem/7120

string = input()

new = string[0]

for i in range(1, len(string)):
    if new[-1] != string[i]:
        new += string[i]

print(new)