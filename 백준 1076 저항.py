# https://www.acmicpc.net/problem/1076

# lst = ["black", "brown", "red", "orange", "yellow",
#     "green", "blue", "violet", "grey", "white"]
# res = ""

# for i in range(3):
#     color = input()
#     for j in range(10):
#         if lst[j] == color:
#             if i == 2:
#                 res = int(res) * int(str(1) + ('0' * j))
#             else:
#                 res += str(j)
                
# print(int(res))


lst = ["black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"]

color1 = lst.index(input())
color2 = lst.index(input())
color3 = lst.index(input())

print(int(str(color1) + str(color2)) * (10 ** color3))