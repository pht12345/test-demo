L = [1, 3, 5, 7, 9, 11]
def square_of_sum(L):
    result = 0
    for num in L:
        result = result + num*num
    return result
print(square_of_sum(L))
