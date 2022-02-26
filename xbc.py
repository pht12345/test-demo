
def func(x):
    z=0
    y=1
    if  isinstance(x,tuple):
        for l in x:
            y=y*l
    else:
        for m in x:
            z=m+z
    return y,z
x=(1,2,3,4,5)
for i in func(x):
    if i>1:
     print(i)
