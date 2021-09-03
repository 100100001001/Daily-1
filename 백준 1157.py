# 백준 단어 공부 1157 https://www.acmicpc.net/problem/1157

word = input().upper()
lst = list(set(word))
cnt = [ word.count(i) for i in lst ]
max_lst = [ lst[i] for i in range(len(lst)) if cnt[i] == max(cnt) ]
print( *max_lst if len(max_lst) == 1 else  "?" )


# word = input().upper()
# lst = list(set(word))
# cnt = [ word.count(i) for i in lst ]

# max_cnt = max(cnt)

# max_lst = []

# for i in range(len(lst)):
#     if cnt[i] == max_cnt:
#         max_lst.append(lst[i])

# if len(max_lst) == 1:
#     print(*max_lst)
# else:
#     print("?")