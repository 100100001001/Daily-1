a, b, v = map(int, input().split())

day = (v - b) // (a - b)

print( day if (v - b) % (a - b) == 0 else day+1 )