i=0
j=1
while j<101:
    i=i+j
    j=j+1
print(i)
def sumok(n):
    if n==1:
        return 1
    return n + sumok(n - 1)
print(sumok(100))
