# https://www.acmicpc.net/problem/2547

t = int(input())
for _ in range(t):
    _ = input()
    student = int(input())

    candy = [ int(input()) for _ in range(student) ]

    if sum(candy) % student == 0:
        print("YES")

    else:
        print("NO")