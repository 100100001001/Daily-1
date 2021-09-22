# https://www.acmicpc.net/problem/2890

r, c = map(int, input().split()) # r행 / c열

kayak = [ input() for _ in range(r) ] # [ S.....111F, S....222.F, ... ]

lst = []
for i in range(r):
    cnt = 1
    for _ in range(c):
        if kayak[i][-1].isdigit():
            lst.append( [kayak[i][-1], cnt, 1] )
            break
        if kayak[i][-1] == '.':
            cnt += 1
        kayak[i] = kayak[i][:-1]

lst.sort(key=lambda x:x[1])

rank = 2
for i in range(1, 9):
    if lst[i-1][1] == lst[i][1]:
        lst[i][2] = rank-1
    else:
        lst[i][2] = rank
        rank += 1

lst.sort(key=lambda x:x[0])

for i in lst:
    print(i[2])
