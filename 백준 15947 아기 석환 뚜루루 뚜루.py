# https://www.acmicpc.net/problem/15947

song = '''
baby sukhwan tururu turu
very cute tururu turu
in bed tururu turu
baby sukhwan
'''

lst = song.split()

N = int(input()) -1
k = N // len(lst)

if N % 14 in [3, 7, 11]:
    print(f'tu+ru*{k+1}' if k >= 4 else 'turu'+ 'ru'*k)
elif N % 14 in [2, 6, 10]:
    print(f'tu+ru*{k+2}' if k >= 3 else 'tururu'+ 'ru'*k)
else:
    print(lst[N % 14])