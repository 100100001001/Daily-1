# https://www.acmicpc.net/problem/1032

n = int(input())
cmd1 = list(input())

for _ in range(n-1):
    cmds = list(input())
    
    for i in range(len(cmd1)):
        if cmd1[i] != cmds[i]:
            cmd1[i] = "?"
        
print(*cmd1, sep="")