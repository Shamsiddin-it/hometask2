# import datetime
# def halowen(a):
#     year, month, day=map(int, a)
#     new=datetime.date(year, month, day)
#     if new.day==31 and new.month==10:
#         print("Bonfire toffee")
#     else:
#         print("toffee")
# a=input()
# b=a.split('/')
# halowen(b)

# ---------------------------------------------

# import datetime
# def century(a):
#     year=int(a)
#     new=datetime.date(year,1,1)
#     print((new.year-1)//100+1)
# a=input()
# century(a)

# -----------------------------------------------

# from datetime import datetime as dt, timedelta
# def aftermonth(a):
#     year=int(a[0])
#     months=int(a[1])
#     new = dt(year,2,1)
#     new2=new+timedelta(days=30*months)
#     print(new2.year)
# a=input().split()
# aftermonth(a)

# ------------------------------------------------

# import datetime
# def conver(a):
#     month,day,year=map(int, a)
#     new=datetime.date(year,month,day)
#     new2=f"{new.year}{new.day}{new.month}"
#     print(new2)
# a=input().split('/')
# conver(a)

# ---------------------------------------------------

# import datetime
# def milkcoffe(a):
#     year,month,day=map(int, a)
#     new=datetime.date(year,month+1,day)
#     print(new.day==24 and new.month==12) 
# a=input().split()
# milkcoffe(a)