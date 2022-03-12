from collections import deque

de_queue = deque(['Mon', 'Tue', 'Wed'])
print(de_queue)
de_queue.append('Thu') # Add element from Right/last
de_queue.appendleft('Sun') # Add element from left/first
print(de_queue)

print("=====PRINT EVERYTHING BEFORE REMOVAL======")
for day in de_queue:
    print(day)

print("Removed from Right : {}".format(de_queue.pop()))
print("Removed from Left : {}".format(de_queue.popleft()))
