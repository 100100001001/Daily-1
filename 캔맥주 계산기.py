def cal():
    try : 
        print("=====♬=============")
        print("========♬==========")
        print("♬ 캔맥주를 마시자 ♬")
        print("=======♬===========")
        print("===============♬===")

        print("1-국산맥주(3000원), 2-해외맥주(3500원)")
        ch = input("무슨 맥주 마실건가요?(숫자로 입력해주세요) ")

        if ch == '1' or ch == '2':
            money = int(input("얼마 있나요? "))
            
            if ch == '1':
                if money < 3000:
                    print("맥주는.. 담에 먹으렴..")
                else:
                    beer = money//3000
                    print("와! {0}캔 먹을 수 있다!".format(beer))
                    ch = money-(beer*3000)
                    if ch > 0:
                        print("남은 돈 {0}원! 안주 사먹어!".format(ch))

            elif ch == '2':
                if 3500 > money >= 3000:
                    print("국산맥주 1캔 마시는 건 어때요!?")
                elif money < 3500:
                    print("맥주는.. 담에 먹으렴..")
                else:
                    beer = money//3500
                    print("와! {0}캔 먹을 수 있다!".format(beer))
                    ch = money-(beer*3500)
                    if ch > 0:
                        print("남은 돈 {0}원! 안주 사먹어!".format(ch))

        else:
            print("")
            print("=====================")
            print("보기에서 입력해주세요")
            print("=====================")
            print("")
            cal()

    except Exception as all_e:
        print("="*20)
        print("에러코드 -",type(all_e))
        print("에러가 발생했습니다.")
        print("아래 번호로 연락주세요.")
        print("000-0000-0000")
        print("="*20)

    finally:
        print("좋은 하루 보내세요!")
        
cal()