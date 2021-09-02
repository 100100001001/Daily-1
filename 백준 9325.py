# 백준 9325 얼마? https://www.acmicpc.net/problem/9325

test_case = int(input())

for _ in range(test_case):
    price = int(input())
    option = int(input())

    for _ in range(option):
        pick, pick_price = map(int, input().split())
        price += pick * pick_price

    print(price)
    
# for _ in range(int(input())):
#     price = int(input())

#     for _ in range(int(input())):
#         pick, pick_price = map(int, input().split())
#         price += pick * pick_price

#     print(price)