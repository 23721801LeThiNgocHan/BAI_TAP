# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:33:26 2024

@author: Student
"""
discout=92/100
a=float(input("So km quang duong di duoc "))
if a<=1:
    st=20.000
    print("so tien ",st)
elif a<= 3:
    st=a*13.000
    print("so tien", st)
elif 4<=a<=8:
    st= 3*13.000 + (a-3)*12.000
    print("so tien",st)
elif 8< a:
    st= 3*13.000 + 5*12.000 + (a-8)*10.000
    print("so tien",st)
    if st > 100.000:
       TT =st*discout
       print("Tong tien",TT)

