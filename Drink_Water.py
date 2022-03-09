def day_water():
    global d_water
    s = input("성별을 입력하세요(F/M) : ")
    w = int(input("몸무게를 입력하세요 : "))
    if s in ['F', 'f']:
        d_water = (w * 30)//14
        print("하루에 {}모금 마시세요!".format(d_water))
    elif s in ['M', 'm']:
        d_water = (w * 30)//21
        print("하루에 {}모금 마시세요!".format(d_water))
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        day_water()
def drink_water():
    day_water()
    r_water = d_water
    while True:
        water = int(input("얼마나 마셨나요? "))
        r_water = r_water - water
        if water == 0 :
            print("물 드십시오.")
        else:
            if r_water <= 0:
                print("참 잘했어요! 내일도 잊지말자, 물!")
                break
            else:
                print("잘했어요! 이제 {}모금만 마시면 되겠네요~!".format(r_water))
drink_water()