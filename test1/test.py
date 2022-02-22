x=0
def greet(s="world.") :
    return "hello," + s
print(greet())
print(greet("justin."))
def average(*args):
    sum = 0
    if args:
     for item in args:
        sum += item
        avg = sum / len(args)
    else:
        avg=0
    return avg
print(average(5, 6))
print(average(7, 2, 2, 3, 4))
print(average())