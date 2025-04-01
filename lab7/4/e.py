import math

x = int(input())
ans = 1
count = 0
while ans < x:
    if ans <= x:
        count += 1
    ans *= 2
print(count)
    
    