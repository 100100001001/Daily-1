# 백준 8949 대충 더해 https://www.acmicpc.net/problem/8949



A, B = input().split()

a, b = len(A), len(B)

if a > b:
    B = '0'*(a-b) + B
elif a < b:
    A = '0'*(b-a) + A

add = ''

for i in range(a):
    add += str(int(A[i]) + int(B[i]))

print(add) 




# def sol(A, B):

#     a, b = len(A), len(B)

#     if a > b:
#         B = '0'*(a-b) + B
#     elif a < b:
#         A = '0'*(b-a) + A

#     add = ''

#     for i in range(len(A)):
#         add += str(int(A[i]) + int(B[i]))

#     return add    


# A, B = input().split()
# print(sol(A, B))