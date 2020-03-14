# Write your code here :-)
from datetime import date

dob = input("DoB [yyyymmdd]: ")
print(dob)
if int(dob) < 10000000:
    raise RuntimeError("Invalid date of birth")
yyyy = dob[:4]
# yyyy = ""
# for i in range(4):
#     yyyy += dob[i]
print(yyyy)
mm = dob[4:6]
print(mm)
dd = dob[6:]
print(dd)

year = int(yyyy)
month = int(mm)
day = int(dd)
print(year, month, day)

today = date.today()
tyear = today.year
tmonth = today.month
tday = today.day
print(tyear, tmonth, tday)