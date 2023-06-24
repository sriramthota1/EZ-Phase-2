from queue import LifoQueue

s=LifoQueue(maxsize=3)
print(s.qsize())

s.put('a')
s.put('b')
s.put('c')


print(s.full())
print(s.qsize())
print(s.get())
print(s.get())
print(s.get())

print(s.empty())

print("")



import queue
a=queue.Queue()
b=queue.Queue()

for i in range(5):
    b.put(i)
print(a.empty())
print(b.empty())



import queue
L=queue.Queue(maxsize=5)
L.put(10)
L.put(20)

print(type(L))


