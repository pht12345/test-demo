# Enter a code
from tkinter import Scrollbar

people = 62
if people < 3:
    print('婴儿')
elif people>=6 and people<18:
    print('青少年')
elif  people>18 and people<60:
    print('成年人')
elif  people>60:
    print('老年人')
else : 
     print('儿童')         
