import zoneinfo
from datetime import date
from datetime import datetime as dt

t = date(2022, 3, 10)
print("Today {}".format(t))

n = dt.now()
print("Now {}".format(n))

s = n.strftime("%A %m %Y")
print('\nExample 1:', s)

s = n.strftime("%d/%m/%Y")
print("dd/mm/yyyy {}".format(s))

s = n.strftime("%Y/%m/%d")
print("yyyy/mm/dd {}".format(s))
