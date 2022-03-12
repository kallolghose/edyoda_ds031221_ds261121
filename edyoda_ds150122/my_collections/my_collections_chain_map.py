from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 2, 'd': 3}
d3 = {'d': 5, 'f': 4}

cm = ChainMap(d1, d2, d3)
print(cm)
print(list(cm.keys()))
print(list(cm.values()))

