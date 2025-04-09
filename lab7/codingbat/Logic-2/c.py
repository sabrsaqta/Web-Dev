def thesum(a, b, c):
    sum = 0
    if a == 14:
        sum = 0
    elif b == 14:
        sum += a
    elif c == 14:
        sum = a + b
    else:
        sum = a + b + c
    return sum


a, b, c = int(input()), int(input()), int(input())

print(thesum(a, b, c))