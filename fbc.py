s=0
num =1
while num<1000:
    if num %2==0  :
        s+=num
        num = num + 1
    else:
         num=num+1
         continue # 当num不为偶数时，跳过后续循环代码，继续下一次循环
print(s)