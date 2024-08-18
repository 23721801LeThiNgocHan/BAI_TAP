# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:32:18 2024

@author: PC
"""

print("kiem tra tinh hop le ngay thang nam")
n=float(input("nhap nam: "))
t=float(input("nhap thang: "))
if t<1 and t>12:
    print("Khong hop le")
d=float(input("nhap ngay: "))
if d<1 and d>31:
    print("Khong hop le")
if n%4 == 0 and n%100 !=0 or n%400 == 0:
    print("Co nam nhuan")
    if t==2:
        print("Thang co 29 ngay")
        if d>29:
            print("Khong hop le")
else:
    print("Nam khong phai la nam nhuan")
    if t==2:
        print("Thang co 28 ngay")
        if d>28:
            print("Khong hop le")
        elif t==1 or t==3 or t==5 or t==7 or t==8 or t==10 or t==12:
            print("Thang co 31 ngay")
        elif t==4 or t==6 or t==9 or t==11:
            print("Thang co 31 ngay")
            if d>30:
                print("Khong hop le")