# https://www.acmicpc.net/problem/1920

def binary_search(n, n_lst, i):
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2
        if n_lst[mid] == i:
            return 1
        elif n_lst[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()

m = int(input())
m_lst = list(map(int, input().split()))

for i in m_lst:
    print(binary_search(n, n_lst, i))