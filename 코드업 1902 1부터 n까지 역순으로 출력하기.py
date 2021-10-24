# https://codeup.kr/problem.php?id=1902

def recursion(n):
    if n == 1:
        return n
    print(n)
    return recursion(n-1)

n = int(input())
print(recursion(n))