# 13458 시험 감독 https://www.acmicpc.net/problem/13458


exam_room = int(input()) # 시험장 수
N = map(int, input().split()) # 시험장별 응시자 수
general, assistant = map(int, input().split()) # 총감독관(1명) / 부감독관(여러명 가능) 감시 가능 수
total_cnt = 0

for i in N: # 시험장별 응시자 수를 하나씩 꺼내옴
    i -= general # 응시자 수 - 총 감독관
    cnt = 1 # 카운트를 한번 세어 줌
    if i > 0 : # 감시할 응시자 수가 남았다면
        cnt += i // assistant # 부감독관으로 나눠주고 몫을 카운트에 더해 줌
        if i % assistant != 0 : # 감시할 응시자 수가 남았다면 
            cnt += 1 # 카운트를 한번 더 해줌
    total_cnt += cnt
print(total_cnt)