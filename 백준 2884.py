# 2884 ěëěęł https://www.acmicpc.net/problem/2884

H, M = map(int, input().split())

if M >= 45 :
    print(H, M-45)
elif M < 45 and H > 0:
    print(H-1, M+15)
else:
    print(23, M+15)