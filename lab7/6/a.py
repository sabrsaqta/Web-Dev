def myfunc(a, b, c, d):
    smallest = d
    if a < smallest:
        smallest = a
    if b < smallest:
        smallest = b
    if c < smallest:
        smallest = c
    print(smallest)



lst = list(map(int, input().split()))
a = lst[0]
b = lst[1]
c = lst[2]
d = lst[3]

myfunc(a, b, c, d)