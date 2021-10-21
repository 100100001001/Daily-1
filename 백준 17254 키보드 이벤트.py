# https://www.acmicpc.net/problem/17254


keyboard, push = map(int, input(). split())

input_key =  [ input().split() for _ in range(push) ]
# [['1', '0', 'A'], ['2', '1', 'P'], ['1', '2', 'L'], ['2', '4', 'E'], ['3', '0', 'P']]

# input_key = sorted(input_key, key = lambda x: int(x[0]))
# input_key = sorted(input_key, key = lambda x: int(x[1]))

input_key = sorted(input_key, key = lambda x: [int(x[1]), int(x[0])])

for i in input_key:
    print(i[2], end='')