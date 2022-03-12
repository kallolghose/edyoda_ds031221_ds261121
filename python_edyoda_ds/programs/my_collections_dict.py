from collections import OrderedDict, ChainMap
from datetime import date
from datetime import datetime as dt


print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

d['b'] = 2.01

for (key, val) in d.items():
    print("{} : {}".format(key, val))

print("=============================")

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for (key, val) in od.items():
    print("{} : {}".format(key, val))


# ==========================================================================
d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
d4 = {'c': 10, 'd': 40} 
    
# Defining the chainmap  
c = ChainMap(d1, d2, d3)  
       
print(c)
print(c.maps)
print(list(c.keys()))
print(list(c.values()))
print(c['d'])

"""
Datetime ============================
"""

my_date = date(1996, 12, 11)
print("Date passed as argument is", my_date)
today = date.today()
print("Today's date is", today)

date_time = dt.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)

# Getting current date and time
now = dt.now()
 
string = dt.isoformat(now)
print("ISO Format {}".format(string))

"""
Format based on input
"""
 
# Getting current date and time
now = dt.now()
print("Without formatting", now)
 
# Example 1
s = now.strftime("%A %m %Y")
print('\nExample 1:', s)
 
# Example 2
s = now.strftime("%a %m %y")
print('\nExample 2:', s)
 
# Example 3
s = now.strftime("%I %p %S")
print('\nExample 3:', s)
 
# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)