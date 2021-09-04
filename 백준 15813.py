# 15813 너의 이름은 몇 점이니? https://www.acmicpc.net/problem/15813

_ = input() # 이름의 길이
name = input() # 이름 ## SOYOON
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
score = 0

for i, alp in enumerate(alphabet): ## 0, A / 1, B ...
    if alp in name: ## O 가 name 에 있다면 i = 15
        cnt = name.count(alp) ## O 는 3개 있으니까 cnt = 3
        score += (cnt * i) + cnt ## score += 3 * 15 + 3
        # i가 0에서 시작했기 때문에 개수만큼 1씩 더해줘야함
        
print(score)

# import string
# print(string.ascii_uppercase)