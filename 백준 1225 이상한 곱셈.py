# https://www.acmicpc.net/problem/1225

# 시간초과 ============================
# import sys
# input = sys.stdin.readline

# a, b = input().split()
# add = 0

# for i in a:
#     for j in b:
#         add += int(i) * int(j)

# print(add)
# =====================================

'''
1×3 + 1×4 + 2×3 + 2×4 + 1×3 + 1×4 = 28
(1+2+1)*(3+4) = 28
'''

import sys
input = sys.stdin.readline

a, b = input().split()

a = list(map(int, a))
b = list(map(int, b))

print(sum(a) * sum(b))

