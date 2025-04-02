def myfunc(a, n):
    print(a**n)

a, n = map(float, input().split())
n = int(n)

myfunc(a, n)