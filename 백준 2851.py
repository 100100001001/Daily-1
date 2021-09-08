# 슈퍼 마리오 https://www.acmicpc.net/problem/2851


mashroom = [ int(input()) for _ in range(10) ]

score = 0

for i in mashroom:
    score += i
    if score >= 100:
        if score - 100 > 100 - (score - i) :
            score -= i
        break

print(score)