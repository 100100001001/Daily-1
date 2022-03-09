import random

n = int(input("학생 수를 입력하세요 : "))
col = int(input("세로 줄을 입력하세요 : "))
exc = list(map(int, input("제외할 자리 번호를 입력해주세요(띄어쓰기로 구분해주세요) : ").split()))

student = {}
number = [ i for i in range(1, n+1) ]
random.shuffle(number)

for i in range(n):
    num = number[i]
    if num in exc:
        student[num] = "🌺"
        continue
    name = input("이름을 입력하세요 : ")
    student[num] = name

sort_student = sorted(student.items(), key=lambda x:x[0], reverse=False)

print("""
🌺✨✨🌺✨🌺🌺🌺
🌺✨✨🌺✨✨🌺✨
🌺🌺🌺🌺✨✨🌺✨
🌺✨✨🌺✨✨🌺✨
🌺✨✨🌺✨🌺🌺🌺
""")
for i in range(n):
    if i > 0 and i % col == 0:
        print(end="\n")
    print(sort_student[i], end=" ")