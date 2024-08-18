# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:34:17 2024

@author: PC
"""

def is_leap_year(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400==0)
def is_valid_date(day,month,year):
    if month < 1 or month > 12:
        return False
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month ==2 and is_leap_year(year):
        day_in_month[1]=29
        if day<1 or day > days_in_month[month-1]:
            return False
        return True
    def check_date_format(date_string):
        try:
            if"/" in date_string:
                day,month,year=map(int,date_string.split("/"))
            elif"-" in date_string:
                day,month,year=map(int,date_string.split("/"))
            else:
                return Fale
            if is_valid_date(day,month,year):
                return f"Ngay {day}/{month}/{year} la hop le"
            else:
                return f"Ngay {day}/{month}/{year} khong hop le"
        except ValueError:
                return "Dinh dang ngay thang khong dung"
        date_string = input("Nhap ngay thang nam (dd/mm/yyyy hoac dd-mm-yyyy): ")
        result = check_date_format(date_string)
        print(result)