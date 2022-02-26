s1 = set([1,2,3,4,5])
s2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
if s1.isdisjoint(s2):  
  print('noncoincidence') 
elif s1.issubset(s2):
  print(s1) 
else:  
   for x in s1:
        for y in s2:
             if x==y:
                print(x)
