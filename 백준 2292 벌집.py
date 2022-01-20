n = int(input())

cnt = 1
honeycomb = 1

while n > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1
    
print(cnt)


'''
1, 7, 19, 37, 61
-----------------
6, 12, 18, 24
'''