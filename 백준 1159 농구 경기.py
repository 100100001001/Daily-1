# https://www.acmicpc.net/problem/1159

dic = {}
sol = ""

for _ in range(int(input())):
    name = input()
    
    if dic.get(name[0]):
        dic[name[0]] += 1
    else:
        dic[name[0]] = 1

sort_dic = sorted(dic.items(), key=lambda x: x[0])
for i, j in sort_dic:
    if j >= 5:
        sol += i

print(sol if sol else "PREDAJA")