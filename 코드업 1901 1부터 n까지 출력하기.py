# https://codeup.kr/problem.php?id=1901

n = int(input())

def rec(n):
    if n != 1:
        rec(n-1)
    print(n)

rec(n)