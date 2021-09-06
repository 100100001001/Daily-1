# 9226 도깨비말 https://www.acmicpc.net/problem/9226

vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()
    
    if word == '#':
        break   
        
    for _ in range(len(word)):
        if word[0] in vowel:
            break
        else:
            word += word[0]
            word = word[1:]
            
    print(word + 'ay')