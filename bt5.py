# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:10:13 2024

@author: Student
"""

a=float(input("Nhap canh a= "))
b=float(input("Nhap canh b= "))
c=float(input("Nhap canh c= "))
if a+b>c and a+c>b and b+c>a:
 if a==b and b==c:
    print("Day la tam giac deu")
 elif a==b or b==c or a==c:
    print("Day la tam giac can")
 elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Day la tam giac vuong")
 else:
    print("Day la tam giac thuong")
else:
    print("Day khong phai 1 tam giac")
