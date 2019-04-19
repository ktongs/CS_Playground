from queue import *
# class queue():
#     def __init__(self,):

arr = [1,2,3]

arr.insert(1,4)
# arr.append(2)
# arr.pop()
arr[1] = 5
print(arr.pop())
print(arr)
print(type(arr))

q = Queue(0)
q.put(1)
q.put(2)

print(q.get())
print(q.get())

a = [1,2]
b = [3,4]

print(a+b)