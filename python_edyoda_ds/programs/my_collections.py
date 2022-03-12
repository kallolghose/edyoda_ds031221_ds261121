import collections

de_queue = collections.deque(["Mon", "Tue", "Wed"])
de_queue.append("Thu")
de_queue.appendleft("Sun")

print(de_queue)

print("Popped : {}".format(de_queue.pop()))
print("Popped Left : {}".format(de_queue.popleft()))

print(de_queue)

print(", ".join(val for val in de_queue))

l = ['x','y','z','x','x','x','y', 'z']
_counter = collections.Counter(l)
for (key, val) in _counter.items():
    print("{} : {}".format(key, val))

str = "the quick brown fox jumped over the lazy dog"
_counter.update(str)
print(_counter)

words = str.split(" ")
_counter1 = collections.Counter(words)
print(_counter1)


