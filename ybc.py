def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,2))
x=0
def greet(x):
    if x:
        s='hello,{}'.format(x)
    else:
        s='Hello, world.'
    return s
print (greet(x))
print(greet('justin'))
