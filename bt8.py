# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:26:24 2024

@author: PC
"""
nguoichoi=float(input("Nguoi chon (1.keo,2.bua,3.bao): "))
from random import randint
maychon=randint(1,3)
if maychon==1:
    print("may chon: Keo")
elif maychon==2:
    print("may chon: Bua")
elif maychon==3:
    print("may chon: Bao")
if maychon==nguoichoi:
    print("Hoa nhau")
elif (maychon==1 and nguoichoi==2) or (maychon==2 and nguoichoi==3) or (maychon==3 and nguoichoi==1):
    print("Ban thang")
else:
    print("May thang")
