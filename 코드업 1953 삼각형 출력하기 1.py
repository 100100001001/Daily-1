# https://codeup.kr/problem.php?id=1953


n = int(input())

def triangle(n):
    if n != 1:
        triangle(n-1)
    print('*' * n)

triangle(n)