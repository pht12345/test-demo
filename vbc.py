l = [1,2,3,4,5,6]
def sub_sum(l):
 result1=0
 result2=0
 for num in l:
  if num%2==0:
   result1=result1+num
  else:
   result2=result2+num
 return result1,result2
result1,result2=sub_sum(l)
print('偶数和={}'.format(result1))
print('奇书和={}'.format(result2))
