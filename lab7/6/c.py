def myfunc(x, y):
    if x and not y:
        print(1)
    elif y and not x:
        print(1)
    else:
        print(0)

x, y = map(int, input().split())

myfunc(x, y)