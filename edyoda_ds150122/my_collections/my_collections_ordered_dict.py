from collections import OrderedDict

d = {"a1" : 1, "b1" : 2}
d['b1'] = 3
d['c1'] = 4
for (key, val) in d.items():
    print("{} : {}".format(key, val))


od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for (key, val) in od.items():
    print("{} : {}".format(key, val))
