# https://www.acmicpc.net/problem/5397

'''
2
<<BP<A>>Cd-
ThIsIsS3Cr3t
'''


import sys
input = sys.stdin.readline

for _ in range(int(input())):
    pw = input().strip() # 공백을 제거하지 않으면 틀림!
    left, right = [], [] # '<', '>' 커서를 기준으로 나눠줄거임
    for i in pw:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)

    left.extend(reversed(right))
    # right의 순서가 반대로 돼있어서 reversed
    # extend는 리스트의 각 항목을 넣어줌

    # while right:
    #     left.append(right.pop())

    print(''.join(left))
    # print(*left, sep='')