word = input()

alphabet = [
    'ABC', 'DEF', 'GHI', 'JKL', 'MNO',
    'PQRS', 'TUV', 'WXYZ'
]

time = 0

for i in word:
    for idx, j in enumerate(alphabet):
        if i in j:
            time += idx + 3
            
print(time)