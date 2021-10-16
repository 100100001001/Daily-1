# https://www.acmicpc.net/problem/4673

set_num = set(range(1, 10001))
num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    num.add(i)
    
self_num = sorted(set_num - num)
for i in self_num:
    print(i)