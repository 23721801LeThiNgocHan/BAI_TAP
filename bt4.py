# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:02:08 2024

@author: Student
"""

a=float(input("Nhap canh a= "))
b=float(input("Nhap canh b= "))
c=float(input("Nhap canh c= "))
if a+b>c and a+c>b and b+c>a:
    print("Day la tam giac")
else:
    print("Day khong phai la tam giac")