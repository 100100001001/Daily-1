# 창영이의 일기장 https://www.acmicpc.net/problem/2954

sentence = input()

vowel = 'aeiou'

new_sen = ''
idx = 0

while True:
    if idx == len(sentence):
        break

    if sentence[idx] in vowel:
        idx += 2
    new_sen += sentence[idx]
    idx += 1

print(new_sen)