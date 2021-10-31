# https://www.acmicpc.net/problem/1755

dic = {'0':'zero', '1':'one', '2':'two', '3':'three',
       '4':'four', '5':'five', '6':'six',
       '7':'seven', '8':'eight', '9':'nine'}

m, n = map(int, input().split())
lst = []

for i in range(m, n+1):
    lst.append((i, ''.join(dic[j] for j in str(i))))
    
lst = sorted(lst, key = lambda x: x[1])

for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print()
    print(lst[i][0], end=' ')