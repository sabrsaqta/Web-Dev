import math
x = int(input())
y = int(input())

for i in range(x, y+1):
    if math.sqrt(i) % 1 == 0:
        print(i, end=" ")