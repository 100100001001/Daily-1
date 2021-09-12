# https://www.acmicpc.net/problem/11586

n = int(input())
mirror = [ input() for _ in range(n) ]
angry = int(input())

if angry == 1: # 그대로 출력
    print(*mirror, sep='\n')

elif angry == 2: # 좌/우 반전
    for i in range(n):
        print(mirror[i][::-1])

else: # 상/하 반전
    print(*mirror[::-1], sep='\n')