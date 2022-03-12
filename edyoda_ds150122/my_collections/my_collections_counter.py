from collections import Counter

list = [10, 20, 10, 30, 20, 20]
_counter1 = Counter(list)
for (key, val) in _counter1.items():
    print("{} : {}".format(key, val))

_counter2 = Counter("Hello World !!")
print(_counter2)

str = "the quick brown fox jumped over the lazy dog"
_counter3 = Counter(str.split(" "))
print(_counter3)
