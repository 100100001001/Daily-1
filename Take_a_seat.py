import random

def number():
    global n
    n = int(input("학생 수를 입력하세요 : "))
    print("😉 " * n)

def column():
    global col
    col = int(input("세로 줄을 입력하세요 : "))
    for i in range(1, n+1):
        print(i, end=" ")
        if i % col == 0:
            print(end="\n")
    print("")

def seat():
    global sort_student
    print("제외할 자리 번호를 입력해주세요! 없다면 엔터 치세요~")
    exc = list(map(int, input("띄어쓰기로 구분해주세요 ").split()))
    print("===================================")

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
    print("  ∧  _  ∧")
    print("(。・ω・。)つ━☆・*。")
    print("⊂ ノ ・゜+.")
    print("しーJ °。+ *´¨)")
    print(".· ´¸.·*´¨) ¸.·*¨)")
    print("(¸.·´ (¸.·'*")
    print("짜잔~")

def take_a_seat():
    try:
        print("""
        🌺✨✨🌺✨🌺🌺🌺
        🌺✨✨🌺✨✨🌺✨
        🌺🌺🌺🌺✨✨🌺✨
        🌺✨✨🌺✨✨🌺✨
        🌺✨✨🌺✨🌺🌺🌺
        """)
        print("랜덤 자리배치~!")
        print("")
        number()
        print(n, end="")
        q1 = input("명이 맞나요? [y/n] ")
        if q1 == 'y':
            print("===================================")
            column()
            print("이게 맞나요? 아니면 수정하고 싶나요? 해당 숫자를 입력해주세요")
            q2 = input("[1]이게 맞아요 / [2]앗 가로 줄을 입력했어요 / [3]잘못 눌렀어요 ")
            print("===================================")
            if q2 == '1':
                seat()
                for i in range(n):
                    if i > 0 and i % col == 0:
                        print(end="\n")
                    print(sort_student[i], end=" ")
                print("")
            elif q2 == '2':
                seat()
                tmp = n // col
                for i in range(n):
                    if i > 0 and i % tmp == 0:
                        print(end="\n")
                    print(sort_student[i], end=" ")
                print("")
            elif q2 == '3':
                take_a_seat()
                return
        elif q1 == 'n':
            take_a_seat()
            return
        else:
            print("y/n 중에서 입력해주세요")
            take_a_seat()
            return
    except Exception as all_e:
        print("="*20)
        print("에러코드 - ", type(all_e))
        print("다시 입력해주세요")
        print("="*20)
        take_a_seat()

take_a_seat()
print("====================")
print("🌺 행복한 하루 되세요~! 🌺")
print("헤헤")