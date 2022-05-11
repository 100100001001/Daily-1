# https://www.tmpcmicpc.net/problem/1075

n = input()
f = input()
tmp = "00"

while True:
    n = n[:-2] + tmp
    
    if int(n) % int(f) == 0:
        break
    
    if int(tmp) < 9:
        tmp = "0" + str(int(tmp) + 1)
    else:
        tmp = str(int(tmp) + 1)
        
print(tmp)

# n = input()
# f = int(input())
# tmp = int(n[:-2] + '00')

# while True:
#     if tmp % f == 0:
#         break
#     tmp += 1
        
# print(str(tmp)[-2:])