# https://www.acmicpc.net/problem/2562

num = [ int(input()) for _ in range(9) ]

m = max(num)

print(m)
print(num.index(m)+1)