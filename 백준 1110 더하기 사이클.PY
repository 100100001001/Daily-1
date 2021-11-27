# https://www.acmicpc.net/problem/1110

N = int(input())
num = N
count = 0

while True:
    ten = num // 10
    one = num % 10
    add = (ten + one) % 10
    num = (one * 10) + add    
    count += 1
    if num == N :
        break
    
print(count)