# https://www.acmicpc.net/problem/2530

hour, minute, second = map(int, input().split())
cook = int(input())

second += cook % 60
cook //= 60

if second >= 60:
    second -= 60
    minute += 1

minute += cook % 60
cook //= 60
if minute >= 60:
    minute -= 60
    hour += 1

hour += cook % 24
if hour >= 24:
    hour -= 24

print(hour, minute, second)