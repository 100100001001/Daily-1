# 10814 https://www.acmicpc.net/problem/10814

N = int(input())
age_name = {}

for _ in range(N):
    age, name = input().split()
    if int(age) not in age_name.keys(): # age가 key값에 없다면 딕셔너리에 추가
        age_name[int(age)] = [name]
    else:
        age_name[int(age)].append(name) # {21: ['Junkyu', 'Dohyun'], 20: ['Sunyoung']}

s_age_name = sorted(age_name.items())

for a_n in s_age_name : # (20, ['Sunyoung']) / (21, ['Junkyu', 'Dohyun']) # 타입은 튜플!
    for i in range(len(a_n[1])): # 두번째 값의 길이만큼 for문을 돌림
        print(a_n[0], (a_n[1][i]))